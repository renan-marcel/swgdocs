/**
 * SWG Packet Inspector & Decoder Engine
 * Fully client-side parsing for SOE Protocol & SWG Application packets.
 * Includes complete catalog and schema dissectors for Protocols, Commands, and Controllers.
 */

// Popular / Quick-test Presets
const PRESETS = {
  'AddMapLocationMessage': '02 00 ab 21 74 b6 08 00 74 61 74 6f 6f 69 6e 65 31 b5 f6 05 00 00 00 00 12 00 00 00 4d 00 6f 00 73 00 20 00 45 00 69 00 73 00 6c 00 65 00 79 00 20 00 43 00 61 00 6e 00 74 00 69 00 6e 00 61 00 00 50 9a 44 00 60 e4 c3 05 01',
  'ObjectMenuSelectMessage': '02 00 7c a1 87 26 00 00 00 00 02 00 00 00 14',
  'QuestTaskCounterMessage': '05 00 80 ce 5e 46 04 00 00 00 40 04 00 00 15 cd 5b 07 00 00 00 00 00 00 c9 42 0e 00 6b 69 6c 6c 5f 77 6f 6d 70 5f 72 61 74 73 01 00 00 00 09 00 00 00 57 00 6f 00 6d 00 70 00 20 00 52 00 61 00 74 00 73 00 03 00 00 00 0a 00 00 00',
  'QuestTaskTimerMessage': '05 00 80 ce 5e 46 04 00 00 00 41 04 00 00 15 cd 5b 07 00 00 00 00 00 00 c9 42 0c 00 65 73 63 6f 72 74 5f 74 69 6d 65 72 02 00 00 00 09 00 00 00 54 00 69 00 6d 00 65 00 20 00 4c 00 65 00 66 00 74 00 00 00 f0 42',
  'CraftSelectSchematic': '05 00 80 ce 5e 46 04 00 00 00 0e 01 00 00 15 cd 5b 07 00 00 00 00 00 00 c9 42 1d 01 00 00',
  'CraftRequestSession': '05 00 80 ce 5e 46 04 00 00 00 0f 01 00 00 15 cd 5b 07 00 00 00 00 00 00 c9 42 cf a2 60 53 02 00 00 00 01',
  'ShipHit': '05 00 80 ce 5e 46 04 00 00 00 32 04 00 00 15 cd 5b 07 00 00 00 00 00 00 c9 42 00 00 00 00 00 00 80 3f 00 00 00 00 00 00 7a 43 01 00 00 00 00 00 00 00',
  'UpdateShipOnCollision': '05 00 80 ce 5e 46 04 00 00 00 fd 03 00 00 15 cd 5b 07 00 00 00 00 00 00 c9 42 00 00 00 00 00 00 00 00 00 00 80 3f 00 00 70 41 00 00 00 00 00 00 20 c1 00 00 96 42',
  'Buffs': '05 00 80 ce 5e 46 04 00 00 00 29 02 00 00 15 cd 5b 07 00 00 00 00 00 00 c9 42 cd ab 34 12 2c 01 00 00',
  'SOE_Data_Channel': '00 09 00 14 02 00 ab 21 74 b6 08 00 74 61 74 6f 6f 69 6e 65 31 b5 f6 05 00 00 00 00 12 00 00 00 4d 00 6f 00 73 00 20 00 45 00 69 00 73 00 6c 00 65 00 79 00 20 00 43 00 61 00 6e 00 74 00 69 00 6e 00 61 00 00 50 9a 44 00 60 e4 c3 05 01 b2 4f'
};

if (typeof window !== 'undefined') {
  window.PRESETS = PRESETS;
}


// Global registries initialized from window.SWG_* or defaults
const OPCODES = Object.assign({
  'AB2174B6': { name: 'AddMapLocationMessage', sec: 'protocols', dir: 'S→C', url: '../protocols/AddMapLocationMessage.html', comp: '100%' },
  '7CA18726': { name: 'ObjectMenuSelectMessage', sec: 'protocols', dir: 'C→S', url: '../protocols/ObjectMenuSelectMessage--MESSAGE_TYPE.html', comp: '100%' },
  '80CE5E46': { name: 'ObjControllerMessage', sec: 'controllers', dir: 'C↔S', url: '../controllers/ObjControllerMessage.html', comp: '100%' },
  '00000116': { name: 'CommandQueueEnqueue', sec: 'commands', dir: 'C→S', url: '../commands/CommandQueueEnqueue (00000116).html', comp: '100%' },
  '2A68DE42': { name: 'ChatServerAgent', sec: 'protocols', dir: 'S→C', url: '../protocols/ChatServerAgent.html', comp: '100%' },
  '7E0271EE': { name: 'ConnectToLoginServer', sec: 'protocols', dir: 'C→S', url: '../protocols/ConnectToLoginServer.html', comp: '100%' },
  '9CA80F98': { name: 'AbortTradeMessage', sec: 'protocols', dir: 'S→C', url: '../protocols/AbortTradeMessage.html', comp: '100%' },
  '68A75F0C': { name: 'BaselinesMessage', sec: 'baselines', dir: 'S→C', url: '../baselines/Protocol BaseDelta.html', comp: '100%' },
  '120A477A': { name: 'DeltasMessage', sec: 'deltas', dir: 'S→C', url: '../deltas/Protocol BaseDelta.html', comp: '100%' }
}, (typeof window !== 'undefined' && window.SWG_OPCODES) ? window.SWG_OPCODES : {});

const CONTROLLER_MSGS = Object.assign({
  0x00000440: { name: 'QuestTaskCounterMessage', dir: 'S→C', url: '../controllers/QuestTaskCounterMessage (00000440).html' },
  0x00000441: { name: 'QuestTaskTimerMessage', dir: 'S→C', url: '../controllers/QuestTaskTimerMessage (00000441).html' },
  0x0000010E: { name: 'CraftSelectSchematic', dir: 'C→S', url: '../controllers/CraftSelectSchematic (0000010E).html' },
  0x0000010F: { name: 'CraftRequestSession', dir: 'C→S', url: '../controllers/CraftRequestSession (0000010F).html' },
  0x00000432: { name: 'ShipHit', dir: 'S→C', url: '../controllers/ShipHit (00000432).html' },
  0x000003FD: { name: 'UpdateShipOnCollision', dir: 'C↔S', url: '../controllers/UpdateShipOnCollision (000003FD).html' },
  0x00000229: { name: 'Buffs', dir: 'S→C', url: '../controllers/Buffs (00000229).html' },
  0x0000022A: { name: 'ImageDesignStartMessage', dir: 'C↔S', url: '../controllers/ImageDesignStartMessage (0000022A).html' },
  0x000003FE: { name: 'AboutToHyperspace', dir: 'S→C', url: '../controllers/AboutToHyperspace (000003FE).html' },
  0x000001FD: { name: 'StartingLocationSelectionResult', dir: 'S→C', url: '../controllers/StartingLocationSelectionResult (000001FD).html' },
  0x00000438: { name: 'AskGroupMemberToLaunchIntoSpace', dir: 'C→S', url: '../controllers/AskGroupMemberToLaunchIntoSpace (00000438).html' },
  0x00000439: { name: 'GroupMemberInvitationToLaunchIntoSpaceResponse', dir: 'C→S', url: '../controllers/GroupMemberInvitationToLaunchIntoSpaceResponse (00000439).html' },
  0x000001BF: { name: 'DraftSlotsQueryResponse', dir: 'S→C', url: '../controllers/DraftSlotsQueryResponse (000001BF).html' },
  0x00000167: { name: 'CommandQueueAdd', dir: 'S→C', url: '../controllers/CommandQueueAdd (00000167).html' },
  0x00000117: { name: 'CommandQueueRemove', dir: 'S→C', url: '../controllers/CommandQueueRemove (00000117).html' },
  0x000000E5: { name: 'NetworkId', dir: 'C↔S', url: '../controllers/NetworkId (000000E5).html' },
  0x000000EB: { name: 'NetworkIdPair', dir: 'C↔S', url: '../controllers/NetworkIdPair (000000EB).html' },
  0x0000012D: { name: 'NetworkIdAndTransform', dir: 'C↔S', url: '../controllers/NetworkIdAndTransform (0000012D).html' },
  0x00000071: { name: 'DataTransform', dir: 'C↔S', url: '../controllers/DataTransform (00000071).html' },
  0x000000F1: { name: 'DataTransformWithParent', dir: 'C↔S', url: '../controllers/DataTransformWithParent (000000F1).html' }
}, (typeof window !== 'undefined' && window.SWG_CONTROLLER_MSGS) ? window.SWG_CONTROLLER_MSGS : {});

const COMMAND_CRCS = (typeof window !== 'undefined' && window.SWG_COMMANDS) ? window.SWG_COMMANDS : {};
const CATALOG = (typeof window !== 'undefined' && window.SWG_CATALOG) ? window.SWG_CATALOG : [];

// SOE Protocol Opcodes
const SOE_OPCODES = {
  0x0001: 'SOE Session Request',
  0x0002: 'SOE Session Response',
  0x0003: 'SOE Multi-Channel Connect',
  0x0005: 'SOE Disconnect',
  0x0007: 'SOE Net Status Request',
  0x0008: 'SOE Net Status Response',
  0x0009: 'SOE Reliable Data Channel',
  0x000D: 'SOE Acknowledge',
  0x0011: 'SOE Ordered Data',
  0x0019: 'SOE Multi-Packet Bundle',
  0x001D: 'SOE Ping'
};

// State
let currentBytes = new Uint8Array(0);
let currentDissection = [];

/**
 * Cleans user input and parses hex bytes
 */
function cleanHex(raw) {
  let cleaned = raw.replace(/\/\/.*/g, '');
  cleaned = cleaned.replace(/0x/gi, '');
  cleaned = cleaned.replace(/^[0-9a-f]{4,8}[:\s-]/gim, '');
  cleaned = cleaned.replace(/[^0-9a-fA-F]/g, '');
  if (cleaned.length % 2 !== 0) {
    cleaned = cleaned.slice(0, -1);
  }
  const bytes = new Uint8Array(cleaned.length / 2);
  for (let i = 0; i < cleaned.length; i += 2) {
    bytes[i / 2] = parseInt(cleaned.substr(i, 2), 16);
  }
  return bytes;
}

/**
 * Reads primitives from byte array with DataView
 */
class PacketReader {
  constructor(bytes, offset = 0) {
    this.bytes = bytes;
    this.view = new DataView(bytes.buffer, bytes.byteOffset, bytes.byteLength);
    this.offset = offset;
  }

  remaining() {
    return this.bytes.length - this.offset;
  }

  readUint8() {
    if (this.offset + 1 > this.bytes.length) throw new Error("Unexpected End of Packet");
    const val = this.view.getUint8(this.offset);
    this.offset += 1;
    return val;
  }

  readUint16LE() {
    if (this.offset + 2 > this.bytes.length) throw new Error("Unexpected End of Packet");
    const val = this.view.getUint16(this.offset, true);
    this.offset += 2;
    return val;
  }

  readUint16BE() {
    if (this.offset + 2 > this.bytes.length) throw new Error("Unexpected End of Packet");
    const val = this.view.getUint16(this.offset, false);
    this.offset += 2;
    return val;
  }

  readUint32LE() {
    if (this.offset + 4 > this.bytes.length) throw new Error("Unexpected End of Packet");
    const val = this.view.getUint32(this.offset, true);
    this.offset += 4;
    return val;
  }

  readUint32BE() {
    if (this.offset + 4 > this.bytes.length) throw new Error("Unexpected End of Packet");
    const val = this.view.getUint32(this.offset, false);
    this.offset += 4;
    return val;
  }

  readFloatLE() {
    if (this.offset + 4 > this.bytes.length) throw new Error("Unexpected End of Packet");
    const val = this.view.getFloat32(this.offset, true);
    this.offset += 4;
    return val;
  }

  readUint64LE() {
    if (this.offset + 8 > this.bytes.length) throw new Error("Unexpected End of Packet");
    const low = this.view.getUint32(this.offset, true);
    const high = this.view.getUint32(this.offset + 4, true);
    this.offset += 8;
    const bigVal = (BigInt(high) << 32n) | BigInt(low);
    return bigVal;
  }

  readAscii() {
    if (this.remaining() < 2) throw new Error("Unexpected End of Packet");
    let len = this.readUint16LE();
    if (len === 0xFFFF && this.remaining() >= 4) {
      len = this.readUint32LE();
    }
    if (this.offset + len > this.bytes.length) {
      len = this.remaining();
    }
    const strBytes = this.bytes.subarray(this.offset, this.offset + len);
    this.offset += len;
    let s = "";
    for (let i = 0; i < strBytes.length; i++) {
      s += String.fromCharCode(strBytes[i]);
    }
    return { len, str: s };
  }

  readUnicode() {
    if (this.remaining() < 4) throw new Error("Unexpected End of Packet");
    const charCount = this.readUint32LE();
    const byteLen = charCount * 2;
    if (this.offset + byteLen > this.bytes.length) {
      throw new Error("Unicode string length extends beyond packet size");
    }
    let s = "";
    for (let i = 0; i < charCount; i++) {
      const code = this.view.getUint16(this.offset + i * 2, true);
      s += String.fromCharCode(code);
    }
    this.offset += byteLen;
    return { count: charCount, str: s };
  }
}

/**
 * Formats byte slice as hex string
 */
function bytesToHex(bytes, start, end) {
  let hex = [];
  for (let i = start; i < end; i++) {
    hex.push(bytes[i].toString(16).padStart(2, '0').toUpperCase());
  }
  return hex.join(' ');
}

/**
 * Schema-driven Field Dissector for documented structs
 */
function dissectFieldsBySchema(reader, schemaFields, outFields, bytes, layerName) {
  if (!schemaFields || schemaFields.length === 0) return;

  for (const f of schemaFields) {
    if (reader.remaining() <= 0) break;
    const fName = f.name || 'Field';
    const fType = (f.type || '').toUpperCase().trim();
    const lowerName = fName.toLowerCase();

    // Skip OpCount/Opcode if they were already parsed by outer layer
    if (lowerName === 'opcount' || lowerName === 'opcode' || lowerName === 'operand_count' || lowerName === 'opperand_count') {
      continue;
    }
    if (lowerName === 'operand' || lowerName === 'objconmessage' || lowerName === 'enum message name' || lowerName === 'spacer') {
      continue;
    }

    const start = reader.offset;
    try {
      let valStr = '';
      let displayType = f.type || 'BYTE';

      if (fType === 'SHORT' || fType === 'USHORT' || fType === 'WORD') {
        if (reader.remaining() < 2) break;
        const v = reader.readUint16LE();
        valStr = `${v} (0x${v.toString(16).padStart(4, '0')})`;
      } else if (fType === 'INT' || fType === 'UINT') {
        if (reader.remaining() < 4) break;
        const v = reader.readUint32LE();
        valStr = `${v} (0x${v.toString(16).padStart(8, '0').toUpperCase()})`;
      } else if (fType === 'LONG' || fType === 'ULONG') {
        if (reader.remaining() < 8) break;
        const v = reader.readUint64LE();
        valStr = `0x${v.toString(16).toUpperCase()} (${v.toString()})`;
      } else if (fType === 'FLOAT') {
        if (reader.remaining() < 4) break;
        const v = reader.readFloatLE();
        valStr = `${v.toFixed(3)}`;
      } else if (fType === 'DOUBLE') {
        if (reader.remaining() < 8) break;
        const v = reader.view.getFloat64(reader.offset, true);
        reader.offset += 8;
        valStr = `${v.toFixed(3)}`;
      } else if (fType === 'BYTE' || fType === 'BOOL') {
        if (reader.remaining() < 1) break;
        const v = reader.readUint8();
        valStr = `${v} (0x${v.toString(16).padStart(2, '0')})`;
      } else if (fType === 'SBYTE') {
        if (reader.remaining() < 1) break;
        const v = reader.view.getInt8(reader.offset);
        reader.offset += 1;
        valStr = `${v}`;
      } else if (fType.includes('ASCII') || fType.includes('ASTRING') || fType.includes('CSTRING') || fType.includes('A_STRING')) {
        const s = reader.readAscii();
        valStr = `"${s.str}"`;
        displayType = 'ASCII String';
      } else if (fType.includes('UNICODE') || fType.includes('USTRING') || fType.includes('U_STRING')) {
        const s = reader.readUnicode();
        valStr = `"${s.str}"`;
        displayType = 'UNICODE String';
      } else {
        // Fallback heuristic based on remaining bytes
        if (reader.remaining() >= 4) {
          const v = reader.readUint32LE();
          valStr = `${v} (0x${v.toString(16).toUpperCase()})`;
          displayType = 'INT';
        } else {
          const v = reader.readUint8();
          valStr = `0x${v.toString(16).padStart(2, '0')}`;
          displayType = 'BYTE';
        }
      }

      outFields.push({
        layer: layerName,
        name: fName,
        type: displayType,
        offset: [start, reader.offset],
        hex: bytesToHex(bytes, start, reader.offset),
        value: valStr
      });
    } catch (e) {
      break;
    }
  }
}

/**
 * Main Dissector function
 */
function dissectPacket(bytes) {
  const fields = [];
  let reader = new PacketReader(bytes, 0);

  if (bytes.length < 2) {
    throw new Error("Packet is too short (minimum 2 bytes required)");
  }

  // 1. Check SOE Protocol Layer
  const firstWordBE = (bytes[0] << 8) | bytes[1];
  let isSOE = false;
  let soeOpcodeName = SOE_OPCODES[firstWordBE];

  if (soeOpcodeName && (firstWordBE === 0x0009 || firstWordBE === 0x000D || firstWordBE === 0x0001 || firstWordBE === 0x0003 || firstWordBE === 0x0005 || firstWordBE === 0x001D)) {
    isSOE = true;
    const start = reader.offset;
    const opcodeVal = reader.readUint16BE();
    fields.push({
      layer: 'SOE',
      name: 'SOE Opcode',
      type: 'SHORT (BE)',
      offset: [start, reader.offset],
      hex: bytesToHex(bytes, start, reader.offset),
      value: `0x${opcodeVal.toString(16).padStart(4, '0').toUpperCase()} (${soeOpcodeName})`
    });

    if (firstWordBE === 0x0009 || firstWordBE === 0x000D || firstWordBE === 0x0011) {
      const seqStart = reader.offset;
      const seq = reader.readUint16BE();
      fields.push({
        layer: 'SOE',
        name: 'Sequence Number',
        type: 'SHORT (BE)',
        offset: [seqStart, reader.offset],
        hex: bytesToHex(bytes, seqStart, reader.offset),
        value: `${seq} (0x${seq.toString(16).padStart(4, '0')})`
      });
    }
  }

  // If SOE wrapper, check trailing 2-byte SOE CRC
  let appEnd = bytes.length;
  if (isSOE && bytes.length >= 6) {
    appEnd = bytes.length - 2;
  }

  // 2. Parse SWG Application Layer
  if (reader.offset < appEnd) {
    const opCountStart = reader.offset;
    const operandCount = reader.readUint16LE();

    fields.push({
      layer: 'SWG',
      name: 'Operand_Count',
      type: 'SHORT (LE)',
      offset: [opCountStart, reader.offset],
      hex: bytesToHex(bytes, opCountStart, reader.offset),
      value: `${operandCount} operands`
    });

    // Opcode
    const opStart = reader.offset;
    const opRaw = reader.readUint32BE();
    const opRawLE = ((opRaw & 0xFF) << 24) | ((opRaw & 0xFF00) << 8) | ((opRaw >> 8) & 0xFF00) | ((opRaw >> 24) & 0xFF);
    const opHexBE = opRaw.toString(16).padStart(8, '0').toUpperCase();
    const opHexLE = opRawLE.toString(16).padStart(8, '0').toUpperCase();

    // Check opcode matches against 1,200+ OPCODES database
    let matchedOpcode = OPCODES[opHexBE] ? opHexBE : (OPCODES[opHexLE] ? opHexLE : null);
    let meta = matchedOpcode ? OPCODES[matchedOpcode] : null;

    let opValueStr = `0x${matchedOpcode || opHexBE}`;
    if (meta) {
      const secTag = meta.sec ? ` [${meta.sec.charAt(0).toUpperCase() + meta.sec.slice(1)}]` : '';
      opValueStr += ` (${meta.name}${secTag})`;
    }

    fields.push({
      layer: 'SWG',
      name: 'Opcode',
      type: 'INT',
      offset: [opStart, reader.offset],
      hex: bytesToHex(bytes, opStart, reader.offset),
      value: opValueStr,
      docUrl: meta ? meta.url : null,
      direction: meta ? meta.dir : null
    });

    const effectiveOp = matchedOpcode || opHexBE;

    // 3. Application Payload Dissection
    if (effectiveOp === 'AB2174B6') {
      // AddMapLocationMessage
      try {
        const pStart = reader.offset;
        const planet = reader.readAscii();
        fields.push({ layer: 'Payload', name: 'PlanetName', type: 'ASCII String', offset: [pStart, reader.offset], hex: bytesToHex(bytes, pStart, reader.offset), value: `"${planet.str}"` });

        const nidStart = reader.offset;
        const nid = reader.readUint64LE();
        fields.push({ layer: 'Payload', name: 'NetworkId', type: 'LONG', offset: [nidStart, reader.offset], hex: bytesToHex(bytes, nidStart, reader.offset), value: `0x${nid.toString(16).toUpperCase()} (${nid.toString()})` });

        const locStart = reader.offset;
        const locName = reader.readUnicode();
        fields.push({ layer: 'Payload', name: 'LocationName', type: 'UNICODE String', offset: [locStart, reader.offset], hex: bytesToHex(bytes, locStart, reader.offset), value: `"${locName.str}"` });

        const xStart = reader.offset;
        const x = reader.readFloatLE();
        fields.push({ layer: 'Payload', name: 'X', type: 'FLOAT', offset: [xStart, reader.offset], hex: bytesToHex(bytes, xStart, reader.offset), value: `${x.toFixed(2)}` });

        const zStart = reader.offset;
        const z = reader.readFloatLE();
        fields.push({ layer: 'Payload', name: 'Z', type: 'FLOAT', offset: [zStart, reader.offset], hex: bytesToHex(bytes, zStart, reader.offset), value: `${z.toFixed(2)}` });

        const typeStart = reader.offset;
        const locType = reader.readUint8();
        fields.push({ layer: 'Payload', name: 'LocationType', type: 'BYTE', offset: [typeStart, reader.offset], hex: bytesToHex(bytes, typeStart, reader.offset), value: `${locType} (Icon / Category)` });

        const subStart = reader.offset;
        const subType = reader.readUint8();
        fields.push({ layer: 'Payload', name: 'SubCategory', type: 'BYTE', offset: [subStart, reader.offset], hex: bytesToHex(bytes, subStart, reader.offset), value: `${subType} (Display Flag)` });
      } catch (e) {
        // partial payload handled gracefully
      }

    } else if (effectiveOp === '7CA18726') {
      // ObjectMenuSelectMessage
      try {
        const nidStart = reader.offset;
        const nid = reader.readUint64LE();
        fields.push({ layer: 'Payload', name: 'TargetObjectId', type: 'LONG', offset: [nidStart, reader.offset], hex: bytesToHex(bytes, nidStart, reader.offset), value: `0x${nid.toString(16).toUpperCase()} (${nid.toString()})` });

        const itemStart = reader.offset;
        const item = reader.readUint8();
        fields.push({ layer: 'Payload', name: 'SelectedMenuItem', type: 'BYTE', offset: [itemStart, reader.offset], hex: bytesToHex(bytes, itemStart, reader.offset), value: `${item} (Menu Option Index)` });
      } catch (e) {
        // partial payload handled gracefully
      }


    } else if (effectiveOp === '80CE5E46') {
      // ObjControllerMessage wrapper (Controllers)
      const flagsStart = reader.offset;
      const flags = reader.readUint32LE();
      fields.push({ layer: 'Controller', name: 'Flags', type: 'INT', offset: [flagsStart, reader.offset], hex: bytesToHex(bytes, flagsStart, reader.offset), value: `0x${flags.toString(16).padStart(8, '0')}` });

      const msgIdStart = reader.offset;
      const msgId = reader.readUint32LE();
      const ctrlMeta = CONTROLLER_MSGS[msgId];
      fields.push({
        layer: 'Controller',
        name: 'MessageId',
        type: 'INT',
        offset: [msgIdStart, reader.offset],
        hex: bytesToHex(bytes, msgIdStart, reader.offset),
        value: `0x${msgId.toString(16).padStart(8, '0').toUpperCase()} (${ctrlMeta ? ctrlMeta.name : 'Controller Action'})`,
        docUrl: ctrlMeta ? ctrlMeta.url : null
      });

      const netIdStart = reader.offset;
      const netId = reader.readUint64LE();
      fields.push({ layer: 'Controller', name: 'NetworkId', type: 'LONG', offset: [netIdStart, reader.offset], hex: bytesToHex(bytes, netIdStart, reader.offset), value: `0x${netId.toString(16).toUpperCase()} (${netId.toString()})` });

      const tickStart = reader.offset;
      const tick = reader.readFloatLE();
      fields.push({ layer: 'Controller', name: 'TickCount', type: 'FLOAT', offset: [tickStart, reader.offset], hex: bytesToHex(bytes, tickStart, reader.offset), value: `${tick.toFixed(2)}` });

      // Specialized or schema-driven Controller Payload Dissection
      try {
        if (msgId === 0x00000440) {
          // QuestTaskCounterMessage
          const tStart = reader.offset;
          const taskName = reader.readAscii();
          fields.push({ layer: 'Payload', name: 'TaskName', type: 'ASCII String', offset: [tStart, reader.offset], hex: bytesToHex(bytes, tStart, reader.offset), value: `"${taskName.str}"` });

          const idStart = reader.offset;
          const taskId = reader.readUint32LE();
          fields.push({ layer: 'Payload', name: 'TaskId', type: 'INT', offset: [idStart, reader.offset], hex: bytesToHex(bytes, idStart, reader.offset), value: `${taskId}` });

          const srcStart = reader.offset;
          const src = reader.readUnicode();
          fields.push({ layer: 'Payload', name: 'CounterSource', type: 'UNICODE String', offset: [srcStart, reader.offset], hex: bytesToHex(bytes, srcStart, reader.offset), value: `"${src.str}"` });

          const cntStart = reader.offset;
          const count = reader.readUint32LE();
          fields.push({ layer: 'Payload', name: 'Count', type: 'INT', offset: [cntStart, reader.offset], hex: bytesToHex(bytes, cntStart, reader.offset), value: `${count}` });

          const maxStart = reader.offset;
          const maxCount = reader.readUint32LE();
          fields.push({ layer: 'Payload', name: 'MaxCount', type: 'INT', offset: [maxStart, reader.offset], hex: bytesToHex(bytes, maxStart, reader.offset), value: `${maxCount}` });

        } else if (msgId === 0x00000441) {
          // QuestTaskTimerMessage
          const tStart = reader.offset;
          const taskName = reader.readAscii();
          fields.push({ layer: 'Payload', name: 'TaskName', type: 'ASCII String', offset: [tStart, reader.offset], hex: bytesToHex(bytes, tStart, reader.offset), value: `"${taskName.str}"` });

          const idStart = reader.offset;
          const taskId = reader.readUint32LE();
          fields.push({ layer: 'Payload', name: 'TaskId', type: 'INT', offset: [idStart, reader.offset], hex: bytesToHex(bytes, idStart, reader.offset), value: `${taskId}` });

          const srcStart = reader.offset;
          const src = reader.readUnicode();
          fields.push({ layer: 'Payload', name: 'TimerSource', type: 'UNICODE String', offset: [srcStart, reader.offset], hex: bytesToHex(bytes, srcStart, reader.offset), value: `"${src.str}"` });

          const timeStart = reader.offset;
          const timeLeft = reader.readFloatLE();
          fields.push({ layer: 'Payload', name: 'TimeLeft', type: 'FLOAT', offset: [timeStart, reader.offset], hex: bytesToHex(bytes, timeStart, reader.offset), value: `${timeLeft.toFixed(2)}s` });

        } else if (msgId === 0x0000010E) {
          // CraftSelectSchematic
          const sStart = reader.offset;
          const sIndex = reader.readUint32LE();
          fields.push({ layer: 'Payload', name: 'SchematicIndex', type: 'INT', offset: [sStart, reader.offset], hex: bytesToHex(bytes, sStart, reader.offset), value: `${sIndex} (CRC / Index)` });

        } else if (msgId === 0x0000010F) {
          // CraftRequestSession
          const sStart = reader.offset;
          const sId = reader.readUint64LE();
          fields.push({ layer: 'Payload', name: 'CraftingStationId', type: 'LONG', offset: [sStart, reader.offset], hex: bytesToHex(bytes, sStart, reader.offset), value: `0x${sId.toString(16).toUpperCase()}` });

          const mStart = reader.offset;
          const mode = reader.readUint8();
          fields.push({ layer: 'Payload', name: 'CraftingMode', type: 'BYTE', offset: [mStart, reader.offset], hex: bytesToHex(bytes, mStart, reader.offset), value: `${mode}` });

        } else if (msgId === 0x00000432) {
          // ShipHit
          const dx = reader.readFloatLE(), dy = reader.readFloatLE(), dz = reader.readFloatLE();
          fields.push({ layer: 'Payload', name: 'DirectionVector', type: 'Vector3 (FLOAT x3)', offset: [tickStart + 4, reader.offset], hex: bytesToHex(bytes, tickStart + 4, reader.offset), value: `(${dx.toFixed(2)}, ${dy.toFixed(2)}, ${dz.toFixed(2)})` });

          const dmgStart = reader.offset;
          const dmg = reader.readFloatLE();
          fields.push({ layer: 'Payload', name: 'Damage', type: 'FLOAT', offset: [dmgStart, reader.offset], hex: bytesToHex(bytes, dmgStart, reader.offset), value: `${dmg.toFixed(2)}` });

          const locStart = reader.offset;
          const loc = reader.readUint32LE();
          fields.push({ layer: 'Payload', name: 'HitLocation', type: 'INT', offset: [locStart, reader.offset], hex: bytesToHex(bytes, locStart, reader.offset), value: `${loc}` });

          const wStart = reader.offset;
          const wep = reader.readUint32LE();
          fields.push({ layer: 'Payload', name: 'WeaponIndex', type: 'INT', offset: [wStart, reader.offset], hex: bytesToHex(bytes, wStart, reader.offset), value: `${wep}` });

        } else if (msgId === 0x000003FD) {
          // UpdateShipOnCollision
          const nx = reader.readFloatLE(), ny = reader.readFloatLE(), nz = reader.readFloatLE();
          fields.push({ layer: 'Payload', name: 'CollisionNormal', type: 'Vector3 (FLOAT x3)', offset: [tickStart + 4, reader.offset], hex: bytesToHex(bytes, tickStart + 4, reader.offset), value: `(${nx.toFixed(2)}, ${ny.toFixed(2)}, ${nz.toFixed(2)})` });

          const vStart = reader.offset;
          const vx = reader.readFloatLE(), vy = reader.readFloatLE(), vz = reader.readFloatLE();
          fields.push({ layer: 'Payload', name: 'ReflectionVelocity', type: 'Vector3 (FLOAT x3)', offset: [vStart, reader.offset], hex: bytesToHex(bytes, vStart, reader.offset), value: `(${vx.toFixed(2)}, ${vy.toFixed(2)}, ${vz.toFixed(2)})` });

          const sevStart = reader.offset;
          const sev = reader.readFloatLE();
          fields.push({ layer: 'Payload', name: 'Severity', type: 'FLOAT', offset: [sevStart, reader.offset], hex: bytesToHex(bytes, sevStart, reader.offset), value: `${sev.toFixed(2)}` });

        } else if (msgId === 0x00000229) {
          // Buffs
          const bStart = reader.offset;
          const bCrc = reader.readUint32LE();
          fields.push({ layer: 'Payload', name: 'BuffCrc', type: 'INT', offset: [bStart, reader.offset], hex: bytesToHex(bytes, bStart, reader.offset), value: `0x${bCrc.toString(16).toUpperCase()}` });

          const valStart = reader.offset;
          const bVal = reader.readUint32LE();
          fields.push({ layer: 'Payload', name: 'BuffValue', type: 'INT', offset: [valStart, reader.offset], hex: bytesToHex(bytes, valStart, reader.offset), value: `${bVal} (Duration / Value)` });

        } else if (ctrlMeta && ctrlMeta.fields && ctrlMeta.fields.length > 0) {
          // Dissect controller payload from schema database
          dissectFieldsBySchema(reader, ctrlMeta.fields, fields, bytes, 'Controller Payload');
        }
      } catch (e) {
        // partial controller payload handled gracefully
      }


      // Check trailing controller payload
      if (reader.offset < appEnd) {
        const remStart = reader.offset;
        const remBytes = appEnd - remStart;
        reader.offset = appEnd;
        fields.push({
          layer: 'Payload',
          name: 'Trailing Controller Data',
          type: `BYTES [${remBytes}]`,
          offset: [remStart, appEnd],
          hex: bytesToHex(bytes, remStart, appEnd),
          value: `${remBytes} raw bytes`
        });
      }

    } else if (effectiveOp === '00000116') {
      // CommandQueueEnqueue (Client Commands)
      if (reader.remaining() >= 4) {
        const cStart = reader.offset;
        const actionCounter = reader.readUint32LE();
        fields.push({ layer: 'Command', name: 'ActionCounter', type: 'INT', offset: [cStart, reader.offset], hex: bytesToHex(bytes, cStart, reader.offset), value: `${actionCounter}` });
      }

      if (reader.remaining() >= 4) {
        const crcStart = reader.offset;
        const cmdCrc = reader.readUint32LE();
        const cmdCrcHex = cmdCrc.toString(16).padStart(8, '0').toUpperCase();
        const cmdMeta = COMMAND_CRCS[cmdCrc] || OPCODES[cmdCrcHex];

        let cmdValStr = `0x${cmdCrcHex}`;
        if (cmdMeta) cmdValStr += ` (${cmdMeta.name})`;

        fields.push({
          layer: 'Command',
          name: 'CommandCRC',
          type: 'INT',
          offset: [crcStart, reader.offset],
          hex: bytesToHex(bytes, crcStart, reader.offset),
          value: cmdValStr,
          docUrl: cmdMeta ? cmdMeta.url : null
        });
      }

      if (reader.remaining() >= 8) {
        const tStart = reader.offset;
        const targetId = reader.readUint64LE();
        fields.push({ layer: 'Command', name: 'TargetID', type: 'LONG', offset: [tStart, reader.offset], hex: bytesToHex(bytes, tStart, reader.offset), value: `0x${targetId.toString(16).toUpperCase()} (${targetId.toString()})` });
      }

      if (reader.remaining() >= 4) {
        const opStart = reader.offset;
        const operands = reader.readUnicode();
        fields.push({ layer: 'Command', name: 'CommandOperands', type: 'UNICODE String', offset: [opStart, reader.offset], hex: bytesToHex(bytes, opStart, reader.offset), value: `"${operands.str}"` });
      }

    } else if (meta && meta.fields && meta.fields.length > 0) {
      // Generic Schema-driven Dissector for all other documented Protocols & Commands
      dissectFieldsBySchema(reader, meta.fields, fields, bytes, 'Payload');
    }

    // Trailing payload for any unparsed remaining bytes
    if (reader.offset < appEnd) {
      const remStart = reader.offset;
      const remBytes = appEnd - remStart;
      reader.offset = appEnd;
      fields.push({
        layer: 'Payload',
        name: 'Trailing Payload',
        type: `BYTES [${remBytes}]`,
        offset: [remStart, appEnd],
        hex: bytesToHex(bytes, remStart, appEnd),
        value: `${remBytes} raw bytes`
      });
    }
  }

  // Trailing SOE CRC
  if (isSOE && appEnd < bytes.length) {
    const crcStart = appEnd;
    const crc = (bytes[appEnd] << 8) | bytes[appEnd + 1];
    fields.push({
      layer: 'SOE',
      name: 'SOE CRC16',
      type: 'CRC16 (BE)',
      offset: [crcStart, bytes.length],
      hex: bytesToHex(bytes, crcStart, bytes.length),
      value: `0x${crc.toString(16).padStart(4, '0').toUpperCase()}`
    });
  }

  return fields;
}

if (typeof window !== 'undefined') {
  window.cleanHex = cleanHex;
  window.dissectPacket = dissectPacket;
  window.CATALOG = CATALOG;
  window.OPCODES = OPCODES;
  window.CONTROLLER_MSGS = CONTROLLER_MSGS;
}

/**
 * Render Hex Dump View with Byte Highlighting
 */
function renderHexDump(bytes, container) {
  container.innerHTML = "";
  const total = bytes.length;
  const rows = Math.ceil(total / 16);

  for (let r = 0; r < rows; r++) {
    const rowDiv = document.createElement('div');
    rowDiv.className = 'hex-row';

    const offsetDiv = document.createElement('div');
    offsetDiv.className = 'hex-offset';
    offsetDiv.textContent = (r * 16).toString(16).padStart(6, '0').toUpperCase() + ':';
    rowDiv.appendChild(offsetDiv);

    const bytesDiv = document.createElement('div');
    bytesDiv.className = 'hex-bytes';

    const asciiDiv = document.createElement('div');
    asciiDiv.className = 'hex-ascii';

    for (let i = 0; i < 16; i++) {
      const byteIdx = r * 16 + i;
      const byteSpan = document.createElement('span');
      byteSpan.className = 'hex-byte';

      const asciiSpan = document.createElement('span');
      asciiSpan.className = 'hex-ascii-char';

      if (byteIdx < total) {
        const b = bytes[byteIdx];
        byteSpan.textContent = b.toString(16).padStart(2, '0').toUpperCase();
        byteSpan.dataset.idx = byteIdx;

        const char = (b >= 32 && b <= 126) ? String.fromCharCode(b) : '.';
        asciiSpan.textContent = char;
        asciiSpan.dataset.idx = byteIdx;
      } else {
        byteSpan.innerHTML = '&nbsp;&nbsp;';
        asciiSpan.innerHTML = '&nbsp;';
      }

      bytesDiv.appendChild(byteSpan);
      asciiDiv.appendChild(asciiSpan);
    }

    rowDiv.appendChild(bytesDiv);
    rowDiv.appendChild(asciiDiv);
    container.appendChild(rowDiv);
  }
}

/**
 * Render Dissection Table
 */
function renderDissection(fields, container) {
  container.innerHTML = "";
  if (fields.length === 0) {
    container.innerHTML = '<div style="padding:1.5rem; text-align:center; color:var(--text-muted);">No fields decoded.</div>';
    return;
  }

  const table = document.createElement('table');
  table.className = 'dissection-table';

  table.innerHTML = `
    <thead>
      <tr>
        <th style="width:70px;">Offset</th>
        <th style="width:75px;">Layer</th>
        <th>Field Name</th>
        <th style="width:120px;">Data Type</th>
        <th>Decoded Value</th>
      </tr>
    </thead>
    <tbody></tbody>
  `;

  const tbody = table.querySelector('tbody');

  fields.forEach((f, idx) => {
    const tr = document.createElement('tr');
    tr.className = 'dissection-row';
    tr.dataset.fidx = idx;

    let layerClass = 'badge-swg';
    if (f.layer === 'SOE') layerClass = 'badge-soe';
    else if (f.layer === 'Controller') layerClass = 'badge-controller';
    else if (f.layer === 'Command') layerClass = 'badge-command';

    let valHtml = htmlEscape(f.value);
    if (f.docUrl) {
      valHtml += ` <a href="${f.docUrl}" target="_blank" style="margin-left:0.5rem; font-weight:600; text-decoration:none;">📄 Docs ↗</a>`;
    }

    tr.innerHTML = `
      <td><span class="offset-pill">[${f.offset[0]}..${f.offset[1]-1}]</span></td>
      <td><span class="badge-protocol ${layerClass}">${f.layer}</span></td>
      <td style="font-weight:600;">${htmlEscape(f.name)}</td>
      <td><span class="type-pill">${htmlEscape(f.type)}</span></td>
      <td class="val-mono">${valHtml}</td>
    `;

    tr.addEventListener('mouseenter', () => highlightByteRange(f.offset[0], f.offset[1]));
    tr.addEventListener('mouseleave', () => clearByteHighlight());

    tbody.appendChild(tr);
  });

  container.appendChild(table);
}

function highlightByteRange(start, end) {
  clearByteHighlight();
  const hexDump = document.getElementById('hex-dump-container');
  if (!hexDump) return;

  for (let i = start; i < end; i++) {
    const bSpans = hexDump.querySelectorAll(`[data-idx="${i}"]`);
    bSpans.forEach(el => el.classList.add('field-highlight'));
  }
}

function clearByteHighlight() {
  const hexDump = document.getElementById('hex-dump-container');
  if (!hexDump) return;
  const highlighted = hexDump.querySelectorAll('.field-highlight');
  highlighted.forEach(el => el.classList.remove('field-highlight'));
}

function htmlEscape(str) {
  return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

/**
 * Handle decode execution
 */
function runDecode() {
  const inputEl = document.getElementById('packet-hex-input');
  if (!inputEl) return;
  const input = inputEl.value;
  const statusBanner = document.getElementById('decode-status');
  const hexContainer = document.getElementById('hex-dump-container');
  const tableContainer = document.getElementById('dissection-table-container');

  try {
    const bytes = cleanHex(input);
    if (bytes.length === 0) {
      statusBanner.style.display = 'block';
      statusBanner.className = 'notice-box';
      statusBanner.style.borderLeftColor = '#ef4444';
      statusBanner.style.background = 'rgba(239, 68, 68, 0.08)';
      statusBanner.innerHTML = '<strong>⚠️ Empty Input:</strong> Please enter or paste packet hex bytes.';
      return;
    }

    currentBytes = bytes;
    currentDissection = dissectPacket(bytes);

    statusBanner.style.display = 'block';
    statusBanner.className = 'notice-box';
    statusBanner.style.borderLeftColor = '#22c55e';
    statusBanner.style.background = 'rgba(34, 197, 94, 0.08)';
    statusBanner.innerHTML = `<strong>✅ Decoded Successfully:</strong> Parsed <strong>${bytes.length} bytes</strong> into <strong>${currentDissection.length} protocol fields</strong>.`;

    renderHexDump(bytes, hexContainer);
    renderDissection(currentDissection, tableContainer);

  } catch (err) {
    statusBanner.style.display = 'block';
    statusBanner.className = 'notice-box';
    statusBanner.style.borderLeftColor = '#ef4444';
    statusBanner.style.background = 'rgba(239, 68, 68, 0.08)';
    statusBanner.innerHTML = `<strong>❌ Parse Error:</strong> ${htmlEscape(err.message)}`;
  }
}

/**
 * Load Preset or any Catalog entry
 */
function loadPreset(name) {
  let hex = PRESETS[name];
  if (!hex && CATALOG && CATALOG.length > 0) {
    const item = CATALOG.find(c => c.name === name || c.op === name);
    if (item && item.sample) {
      hex = item.sample;
    }
  }

  if (hex) {
    const inputEl = document.getElementById('packet-hex-input');
    if (inputEl) {
      inputEl.value = hex;
      runDecode();
    }
  }
}

/**
 * Export Dissection as JSON
 */
function copyDecodedJSON() {
  if (!currentDissection || currentDissection.length === 0) {
    alert("Please decode a packet first.");
    return;
  }
  const jsonStr = JSON.stringify(currentDissection, null, 2);
  navigator.clipboard.writeText(jsonStr).then(() => {
    alert("Decoded JSON copied to clipboard!");
  });
}

/**
 * Scroll smoothly to catalog explorer
 */
function scrollToCatalog() {
  const el = document.getElementById('catalog-section');
  if (el) {
    el.scrollIntoView({ behavior: 'smooth' });
    const searchInput = document.getElementById('catalog-search-input');
    if (searchInput) searchInput.focus();
  }
}

/* ============================================================
   Interactive Catalog & Quick Loader Logic
   ============================================================ */

let currentCatalogTab = 'all';
let currentCatalogSearch = '';
let currentCatalogPage = 1;
const ITEMS_PER_PAGE = 30;

function setCatalogTab(tab) {
  currentCatalogTab = tab;
  currentCatalogPage = 1;
  document.querySelectorAll('.catalog-tab').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.tab === tab);
  });
  renderCatalog();
}

function prevCatalogPage() {
  if (currentCatalogPage > 1) {
    currentCatalogPage--;
    renderCatalog();
    document.getElementById('catalog-grid').scrollIntoView({ behavior: 'smooth' });
  }
}

function nextCatalogPage() {
  const filtered = getFilteredCatalog();
  const maxPage = Math.ceil(filtered.length / ITEMS_PER_PAGE) || 1;
  if (currentCatalogPage < maxPage) {
    currentCatalogPage++;
    renderCatalog();
    document.getElementById('catalog-grid').scrollIntoView({ behavior: 'smooth' });
  }
}

function getFilteredCatalog() {
  if (!CATALOG || CATALOG.length === 0) return [];
  const q = currentCatalogSearch.trim().toLowerCase();

  return CATALOG.filter(item => {
    // Tab filter
    if (currentCatalogTab === 'protocols' && item.sec !== 'protocols') return false;
    if (currentCatalogTab === 'commands' && item.sec !== 'commands') return false;
    if (currentCatalogTab === 'controllers' && item.sec !== 'controllers') return false;
    if (currentCatalogTab === 'baselines' && item.sec !== 'baselines' && item.sec !== 'deltas') return false;

    // Search query filter
    if (q) {
      const matchName = item.name.toLowerCase().includes(q);
      const matchOp = item.op.toLowerCase().includes(q);
      const matchSec = item.sec.toLowerCase().includes(q);
      return matchName || matchOp || matchSec;
    }
    return true;
  });
}

function renderCatalog() {
  const grid = document.getElementById('catalog-grid');
  if (!grid) return;

  const filtered = getFilteredCatalog();
  const total = filtered.length;
  const maxPage = Math.ceil(total / ITEMS_PER_PAGE) || 1;
  if (currentCatalogPage > maxPage) currentCatalogPage = maxPage;

  // Update counts and pagination
  const visibleCountEl = document.getElementById('catalog-visible-count');
  if (visibleCountEl) visibleCountEl.textContent = total;

  const pageInfoEl = document.getElementById('catalog-page-info');
  if (pageInfoEl) pageInfoEl.textContent = `Page ${currentCatalogPage} of ${maxPage}`;

  const prevBtn = document.getElementById('catalog-prev-btn');
  const nextBtn = document.getElementById('catalog-next-btn');
  if (prevBtn) prevBtn.disabled = (currentCatalogPage <= 1);
  if (nextBtn) nextBtn.disabled = (currentCatalogPage >= maxPage);

  if (total === 0) {
    grid.innerHTML = '<div style="grid-column: 1 / -1; padding: 2rem; text-align: center; color: var(--text-muted);">No packets match your search.</div>';
    return;
  }

  const startIdx = (currentCatalogPage - 1) * ITEMS_PER_PAGE;
  const pageItems = filtered.slice(startIdx, startIdx + ITEMS_PER_PAGE);

  let html = '';
  pageItems.forEach(item => {
    let secBadgeClass = 'badge-swg';
    let secName = 'Protocol';
    if (item.sec === 'commands') { secBadgeClass = 'badge-command'; secName = 'Command'; }
    else if (item.sec === 'controllers') { secBadgeClass = 'badge-controller'; secName = 'Controller'; }
    else if (item.sec === 'baselines' || item.sec === 'deltas') { secBadgeClass = 'badge-baseline'; secName = item.sec === 'baselines' ? 'Baseline' : 'Delta'; }

    let dirClass = 'badge-sc';
    if (item.dir === 'C→S') dirClass = 'badge-cs';
    else if (item.dir === 'C↔S') dirClass = 'badge-cs';

    const safeName = htmlEscape(item.name);
    const opDisplay = item.op ? `0x${item.op}` : 'No Opcode';
    const sampleType = item.real ? 'Capture' : 'Template';

    html += `
      <div class="catalog-card">
        <div class="catalog-card-top">
          <div class="catalog-card-title">${safeName}</div>
          <span class="badge-protocol ${secBadgeClass}" style="font-size:0.7rem; flex-shrink:0;">${secName}</span>
        </div>

        <div class="catalog-card-badges">
          <span class="offset-pill" style="font-weight:600; color:var(--accent-cyan);">${opDisplay}</span>
          <span class="badge ${dirClass}" style="font-size:0.7rem;">${item.dir}</span>
          <span class="badge badge-sample-present" style="font-size:0.7rem;">${sampleType}</span>
          ${item.fc > 0 ? `<span style="font-size:0.75rem; color:var(--text-muted);">${item.fc} fields</span>` : ''}
        </div>

        <div class="catalog-card-actions">
          <button class="catalog-load-btn" onclick="loadCatalogItem('${encodeURIComponent(item.name)}')">
            ⚡ Load & Dissect
          </button>
          <a href="${item.url}" target="_blank" class="catalog-doc-link">
            <span>Docs</span> <span>↗</span>
          </a>
        </div>
      </div>
    `;
  });

  grid.innerHTML = html;
}

function loadCatalogItem(encodedName) {
  const name = decodeURIComponent(encodedName);
  const item = CATALOG.find(c => c.name === name);
  if (!item || !item.sample) return;

  const inputEl = document.getElementById('packet-hex-input');
  if (inputEl) {
    inputEl.value = item.sample;
    runDecode();
    inputEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
  }
}

// Global initialization
window.addEventListener('DOMContentLoaded', () => {
  // Update Tab Counts from CATALOG if available
  if (CATALOG && CATALOG.length > 0) {
    const totalAll = CATALOG.length;
    const protoCount = CATALOG.filter(c => c.sec === 'protocols').length;
    const cmdCount = CATALOG.filter(c => c.sec === 'commands').length;
    const ctrlCount = CATALOG.filter(c => c.sec === 'controllers').length;
    const baseCount = CATALOG.filter(c => c.sec === 'baselines' || c.sec === 'deltas').length;

    const elTotal = document.getElementById('catalog-total-badge');
    if (elTotal) elTotal.textContent = `${totalAll.toLocaleString()} Packets`;

    const elTabAll = document.getElementById('tab-count-all');
    if (elTabAll) elTabAll.textContent = totalAll;

    const elTabProto = document.getElementById('tab-count-protocols');
    if (elTabProto) elTabProto.textContent = protoCount;

    const elTabCmd = document.getElementById('tab-count-commands');
    if (elTabCmd) elTabCmd.textContent = cmdCount;

    const elTabCtrl = document.getElementById('tab-count-controllers');
    if (elTabCtrl) elTabCtrl.textContent = ctrlCount;

    const elTabBase = document.getElementById('tab-count-baselines');
    if (elTabBase) elTabBase.textContent = baseCount;
  }

  // Hook catalog search
  const searchInput = document.getElementById('catalog-search-input');
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      currentCatalogSearch = e.target.value;
      currentCatalogPage = 1;
      renderCatalog();
    });
  }

  // Initial catalog render
  renderCatalog();

  // Populate first preset by default
  loadPreset('AddMapLocationMessage');
});
