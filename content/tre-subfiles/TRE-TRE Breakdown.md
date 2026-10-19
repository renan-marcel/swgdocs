---
title: TRE:TRE Breakdown
url: https://wiki.swganh.org/index.php/TRE%3ATRE_Breakdown
page_type: Other
opcode: 
revision_id: 257306
last_modified: 
completion: unknown
direction: unknown
sample_status: present
categories: []
templates: ['Template:Box TREformats']
---

# TRE:TRE Breakdown

## Notices
_none_

## Description
_none_

## Struct
| Type | Name |
| --- | --- |
| http | //download.nvidia.com/developer/NVTextureSuite/Photoshop_Plugins_7.83.0629.1500.exe |
| http | //msdn.microsoft.com/library/default.asp?url=/library/en-us/directx9_c/dx9_graphics_reference_dds_file.asp |

## Variable Descriptions
_none_

## Notes
_none_

## Tags
_none_

## Sample Packet
```
rollout SWG_roll "Model importer" (
fn readInvLong f = (
  t1 = readbyte f #unsigned
  t2 = readbyte f #unsigned
  t3 = readbyte f #unsigned
  t4 = readbyte f #unsigned
  return (t4+t3*0x100+t2*0x10000+t1*0x1000000)
)

fn readFORM f = (
  ofsForm = readInvLong f
  hdr = readlong f
  return hdr
)

fn readPoint3 f sc = (
  datasize = readInvLong f
  PT3Ary = #()
  testbyte = readlong f
  fseek f -4 #seek_cur
  if (testbyte<65536)AND(testbyte>=0) then (
   for i = 1 to (datasize/16) do (
    idx = 1 + (readlong f)
    vx = (readfloat f) * sc
    vy = (readfloat f) * sc
    vz = (readfloat f) * sc
    PT3Ary[idx] = [vx,-vz,vy]   
   )
   for i = 1 to PT3Ary.count do
    if PT3Ary[i] == undefined then PT3Ary[i] = [0,0,0]
  ) else (
   for i = 1 to (datasize/12) do (
    vx = (readfloat f) * sc
    vy = (readfloat f) * sc
    vz = (readfloat f) * sc
    append PT3Ary [vx,-vz,vy]   
   )
  )
  return PT3Ary
)

fn readTCSD f = (
  datasize = readInvLong f
  PT2Ary = #()
  for i = 1 to (datasize/8) do (
   vx = readfloat f
   vy = 1- (readfloat f)
   append PT2Ary [vx,vy,0]   
  )
  return PT2Ary
)

fn readPIDX f = (
  IndexAry = #()
  datasize = readInvLong f
  numIndex = readlong f
  for i = 1 to numIndex do append IndexAry (1+(readlong f))
  return IndexAry
)

fn readNIDX f = (
  IndexAry = #()
  datasize = readInvLong f
  for i = 1 to (datasize/4) do append IndexAry (1+(readlong f))
  return IndexAry
)

fn readOITL f = (
  IdxAry = #()
  Int3Ary = #()
  datasize = readInvLong f
  numdata = readlong f
  for i = 1 to numdata do (
   append IdxAry (1+(readshort f))
   f1 = 1 + (readlong f)
   f2 = 1 + (readlong f)
   f3 = 1 + (readlong f)
   append Int3Ary [f1,f2,f3]
  )
  return #(IdxAry,Int3Ary)
)

fn readITL f = (
  Int3Ary = #()
  datasize = readInvLong f
  numdata = readlong f
  for i = 1 to numdata do (
   f1 = 1 + (readlong f)
   f2 = 1 + (readlong f)
   f3 = 1 + (readlong f)
   append Int3Ary [f1,f2,f3]
  )
  return #(undefined,Int3Ary)
)

fn buildmesh VTary FCary NLary UVary PIDXary NIDXary = (
  for i = 1 to PIDXary.count do PIDXary[i] = VTary[(PIDXary[i])]
  for i = 1 to NIDXary.count do NIDXary[i] = NLary[(NIDXary[i])]
  if FCary[1] == undefined then  msh = mesh vertices:PIDXary faces:FCary[2]
  else msh = mesh vertices:PIDXary faces:FCary[2] materialIDs:FCary[1]
  msh.numTVerts = UVary.count
  buildTVFaces msh
  for j = 1 to UVary.count do setTVert  msh j UVary[j]
  for j = 1 to FCary[2].count do setTVFace msh j FCary[2][j]
  for j = 1 to NIDXary.count do setNormal msh j NIDXary[j]
  return msh
)
  ----------------------------------------------------------------------------
fn readDATA f numData sc = (
  datasize = readInvLong f
  if datasize < 8 then (
   fseek f datasize #seek_cur
   return undefined
  )
  VTary = #()
  NLary = #()
  UVary = #()
  sizeElement = datasize/numData
  --format "V:% @[%]\n" sizeElement (ftell f)
  for i = 1 to numData do (
   vx = (readfloat f)*sc;    vy = (readfloat f)*sc;    vz = (readfloat f)*sc
   nx = readfloat f;    ny = readfloat f;    nz = readfloat f
   --
   byteRead = 32
   case sizeElement of (
    36: ( readlong f ; byteRead = 36 )
    52: ( readlong f ; byteRead = 36 )
    56: ( fseek f 16 #seek_cur ; byteRead = 48 )
    default: byteRead = 32
   )
   vu = readfloat f;    vv = 1-(readfloat f)
   fseek f (sizeElement-byteRead) #seek_cur
   --
   append VTary [vx,-vz,vy]
   append NLary [nx,-nz,ny]
   append UVary [vu,vv,0]
  )
  return #(VTary,NLary,UVary)
)
fn readINDX f = (
  FCary = #()
  datasize = readInvLong f
  numIndex = readlong f
  sizeElement = datasize / numIndex
  for i = 1 to (numIndex/3) do (
   if sizeElement == 2 then (
    f1 = 1 + (readshort f #unsigned)
    f2 = 1 + (readshort f #unsigned)
    f3 = 1 + (readshort f #unsigned)
   ) else if sizeElement == 4 then (
    f1 = 1 + (readlong f #unsigned)
    f2 = 1 + (readlong f #unsigned)
    f3 = 1 + (readlong f #unsigned)
   ) else messagebox "error in face index"
   append FCary [f1,f2,f3]
  )
  return FCary
)
fn buildmesh2 VTary FCary NLary UVary = (
  msh = mesh vertices:VTary faces:FCary
  msh.numTVerts = UVary.count
  buildTVFaces msh
  for j = 1 to UVary.count do setTVert  msh j UVary[j]
  for j = 1 to FCary.count do setTVFace msh j FCary[j]
  for j = 1 to NLary.count do setNormal msh j NLary[j]
  return msh
)

--GUI--
spinner fscale "Scale : " fieldwidth:60 range:[0.001, 1000, 1]
button impMGN "Import   MGN / MSH" width:150 Height:25 align:#center
label lbl1 ""
label lbl2 "by Fatduck" align:#right

on impMGN pressed do (
  fname = getOpenFileName caption:"Select Star Wars Galaxies Model file" types:"MGN File (*.mgn)|*.mgn|MSH File (*.msh)|*.msh|All Files (*.*)|*.*|"
  if fname != undefined then (
   f = fopen fname "rb"
   fseek f 0 #seek_end
   ofsEOF = ftell f
   fseek f 0 #seek_set
   VTary = #()
   UVary = #()
   NLary = #()
   FCary = #()
   PIDXary = #()
   NIDXary = #()
   meshFlag = undefined
   infoFlag = undefined
   mshVert = 0
   do (
    header = readlong f
    case header of (
     0x58444E49:
       (
        FCary = readINDX f
        msh = buildmesh2 VTary FCary NLary UVary
       )
     0x41544144:
       (
        rslt = readDATA f mshVert fscale.value
        if rslt != undefined then (
         VTary = rslt[1]
         NLary = rslt[2]
         UVary = rslt[3]
        )
        infoFlag = false
       )
     0x4D524F46:
       (
        flg = readFORM f
        if flg == 0x474D4B53 then meshFlag = true --SKMG
        else if flg == 0x20544C42 then meshFlag = false --BLT
        if flg == 0x41585456 then infoFlag = true --VTXA
       )   
     0x4F464E49:
       (
        if infoFlag == true then (
         fseek f 8 #seek_cur
         mshVert = readlong f
        ) else fseek f (readInvLong f) #seek_cur
       ) 
     0x4E534F50:
       (
        if meshFlag == true then VTary = readPoint3 f fscale.value
        else readPoint3 f fscale.value
       )
     0x4D524F4E:
       (
        if meshFlag == true then NLary = readPoint3 f 1
        else readPoint3 f 1
       )
     0x58444950: PIDXary = readPIDX f
     0x5844494E: NIDXary = readNIDX f
     0x44534354: UVary = readTCSD f
     0x4C54494F:
       (
        FCary = readOITL f
        msh = buildmesh VTary FCary NLary UVary PIDXary NIDXary
       )
     0x204C5449:
       (
        FCary = readITL f
        msh = buildmesh VTary FCary NLary UVary PIDXary NIDXary
       )
     default:
       (
        datasize = readInvLong f
        fseek f datasize #seek_cur
       )
    )--end case
   ) while (ftell f) != ofsEOF
   fclose f
  )--end if fname
)--end on impMGN

)--end rollout SWG_roll

if Fatduck_SWG != undefined then closeRolloutFloater Fatduck_SWG
Fatduck_SWG = newRolloutFloater "Star Wars Galaxies" 200 175 10 70
addRollout SWG_roll Fatduck_SWG
```

## Related Pages
- [[TreFiles History]]
- [[TreFile Template]]
- [[TRE_DDSFileType]]
- [[TRE_QSTFileType]]
- [[TRE_STFFileType]]
- [[TRN (FileFormat)]]

## Other Sections
_none_

## Categories
_none_