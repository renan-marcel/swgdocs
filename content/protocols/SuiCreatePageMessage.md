---
title: SuiCreatePageMessage
url: https://wiki.swganh.org/index.php/SuiCreatePageMessage
page_type: Server Packet
opcode: D44B7259
revision_id: 79396
last_modified: 
completion: 75%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '75% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:A string', 'Template:Byte', 'Template:Long', 'Template:Float', 'Template:Unknown', 'Template:ServerPacket', 'Template:75%']
---

# SuiCreatePageMessage

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Opperand Count |
| INT | opcode |
| INT | window ID |
| A_STRING | UI Script Name |
| INT | List Size |
| BYTE | Change Identifier |
| ... | ... |

## Variable Descriptions
- Operand_Count	     = 2
- Opcode		     = D44B7259

## Notes
- **NOTE:** There is more to this packet to explore!!!

## Tags
- **S→C** - This packet originates on the server.
- **75%** - This packet has been partially reversed.

## Sample Packet
```
02 00                                            //WORLDUPDATE 
59 72 4B D4                                      //SuiCreatePageMessage 
83 52 02 00                                      //UI Window ID
0F 00                                            //String Size(15)
53 63 72 69 70 74 2E 69 6E 70 75 74 42 6F 78     //Script.inputBox
0C 00 00 00                                      //# of Variable Updates
//--------------------cmbInput Is Created Here----------------------------------
05           //change Identifier
00 00 00 00  //Number of Variable Changes  
07 00 00 00  //List Size
00 00        //unknown String 1
01 00 09     //unknown String 2 
19 00                                         //String Size(25) 
6F 6E 47 75 69 6C 64 43 72 65 61 74 65 4E 
61 6D 65 52 65 73 70 6F 6E 73 65              //onGuildCreateNameResponse
08 00                                         //String Size(8)
74 78 74 49 6E 70 75 74                       //txtInput
09 00                                         //String Size(9) 
4C 6F 63 61 6C 54 65 78 74                    //LocalText 
08 00                                         //String Size(8) 
63 6D 62 49 6E 70 75 74                       //cmbInput 
0C 00                                         //String Size(12)
53 65 6C 65 63 74 65 64 54 65 78 74           //SelectedText
//-----------------------cmbInput Is Created Here-------------------------------------------
05            //Change Identifier
00 00 00 00   //num of Variable Changes 
07 00 00 00   //list size
00 00         //unknown string 1 
01 00 0A      //unknown string 2
19 00                                         //String Size(25) 
6F 6E 47 75 69 6C 64 43 72 65 61 74 
65 4E 61 6D 65 52 65 73 70 6F 6E 73 65        //onGuildCreateNameResponse 
08 00                                         //String Size(8)
74 78 74 49 6E 70 75 74                       //txtInput
09 00                                         //String Size(9) 
4C 6F 63 61 6C 54 65 78 74                    //LocalText 
08 00                                         //String Size(8) 
63 6D 62 49 6E 70 75 74                       //cmbInput
0C 00                                         //String Size(12)
53 65 6C 65 63 74 65 64 54 65 78 74           //SelectedText
//------lblPromp's Text Is changed to string/en/guild.stf StringName:create_name_prompt-----------
03                                            //Change Type
01 00 00 00                                   //List Size
19 00 00 00                                   //UNICODE STRING SIZE(25) 
40 00 67 00 75 00 69 00 6C 00 64 00 
3A 00 63 00 72 00 65 00 61 00 74 00 
65 00 5F 00 6E 00 61 00 6D 00 65 00 
5F 00 70 00 72 00 6F 00 6D 00 70 00 74 00     //UNICODE (@guild:create_name_prompt)
02 00 00 00                                   //List Size
10 00                                         //String Size(16) 
50 72 6F 6D 70 74 2E 6C 62 6C 50 
72 6F 6D 70 74                                //Prompt.lblPrompt
04 00                                         //String Size(4)
54 65 78 74                                   //Text 
//-------------Title is changed to @guild:create_name_title-----------------------------------
03                                            //Change Type
01 00 00 00                                   //List Size
18 00 00 00                                   //UNICODE STRING SIZE(24)
40 00 67 00 75 00 69 00 6C 00 64 00 3A 00 
63 00 72 00 65 00 61 00 74 00 65 00 5F 00 
6E 00 61 00 6D 00 65 00 5F 00 74 00 69 00 
74 00 6C 00 65 00                             //UNICODE (@guild:create_name_title ) 
02 00 00 00                                   //List Size
13 00                                         //String Size(19) 
62 67 2E 63 61 70 74 69 6F 6E 2E 6C 62 6C 
54 69 74 6C 65                                //bg.caption.lblTitle 
04 00                                         //String Size(4) 
54 65 78 74                                   //Text
//------------Set Cancel Button to string/en/sui.stf StringName cancel------------
03                                            //Change Type
01 00 00 00                                   //List Size
07 00 00 00                                   //UNICODE STRING SIZE(7) 
40 00 63 00 61 00 6E 00 63 00 65 00 6C 00     //UNICODE (@cancel)
02 00 00 00                                   //List Size
09 00                                         //String Size(9) 
62 74 6E 43 61 6E 63 65 6C                    //btnCancel 
04 00                                         //String Size(4) 
54 65 78 74                                   //Text 
//----------Set Ok Button to string/en/sui.stf StringName ok-----------------------
03                                            //Change Type
01 00 00 00                                   //List Size 
03 00 00 00                                   //UNICODE STRING SIZE(3) 
40 00 6F 00 6B 00                             //@ok
02 00 00 00                                   //List Size
05 00                                         //String Size(5)
62 74 6E 4F 6B                                //btnOk 
04 00                                         //String Size(4)
54 65 78 74                                   //Text 
//---------------This Enables the Input Field-----------------------------------------
03                                           //Change Type
01 00 00 00                                  //List Size
04 00 00 00                                  //String Size(4)
74 00 72 00 75 00 65 00                      //true
02 00 00 00                                  //List Size
08 00                                        //String Size(8)
74 78 74 49 6E 70 75 74                      //txtInput 
07 00                                        //String Size(7) 
45 6E 61 62 6C 65 64                         //Enabled 
//-------------This Makes the Input Field Visable--------------------------------------
03                                           //Change Type
01 00 00 00                                  //List Size
04 00 00 00                                  //UNICODE STRING SIZE(4)
74 00 72 00 75 00 65 00                      //UNICODE (true)
02 00 00 00                                  //List Size 
08 00                                        //String Size(8)
74 78 74 49 6E 70 75 74                      //txtInput
07 00                                        //String Size(7)
56 69 73 69 62 6C 65                         //Visible 
//------------This disables The DropDown Box-----------------------------------------------
03                                          //Change Type
01 00 00 00                                 //List Size
05 00 00 00                                 //UNICODE STRING COUNT (5)
66 00 61 00 6C 00 73 00 65 00               //UNICODE (false)
02 00 00 00                                 //List Size
08 00                                       //String Size(8)
63 6D 62 49 6E 70 75 74                     //cmbInput 
07 00                                       //String Size(7)
45 6E 61 62 6C 65 64                        //Enabled
//------------This Removes the DropDown Box-------------------------------------------------
03                                         //Change Type
01 00 00 00                                //List Size
05 00 00 00                                //UNICODE STRING SIZE(5)
66 00 61 00 6C 00 73 00 65 00              //UNICODE (false)
02 00 00 00                                //List Size
08 00                                      //String Size(8)
63 6D 62 49 6E 70 75 74                    //cmbInput 
07 00                                      //String Size(7)
56 69 73 69 62 6C 65                       //Visible 
//------------Sets The Max Char Count to 127---------------------------------------------------
03                                         //Change Type
01 00 00 00                                //List Size
03 00 00 00                                //UNICODE STRING SIZE (3)
31 00 32 00 37 00                          //UNICODE (127)
02 00 00 00                                //List Size
08 00                                      //String Size(8)
74 78 74 49 6E 70 75 74                    //txtInput
09 00                                      //String Size(9)
4D 61 78 4C 65 6E 67 74 68                 //MaxLength
//-------------Sets cmbInput's Max Chat Count to 127---------------------------------- 
03                                         //Change Type
01 00 00 00                                //List Size
03 00 00 00                                //UNCIDE STRING SIZE (3)
31 00 32 00 37 00                          //UNICODE (127)
02 00 00 00                                //List Size
08 00                                      //String Size(8)
63 6D 62 49 6E 70 75 74                    //cmbInput
09 00                                      //String Size(9) 
4D 61 78 4C 65 6E 67 74 68                 //MaxLength
00 00 00 00 00 00 00 00                    //unk DATA 1
00 00 00 00                                //unk DATA 2
00 00 00 00 00 00 00 00                    //unk DATA 3
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 75% Complete