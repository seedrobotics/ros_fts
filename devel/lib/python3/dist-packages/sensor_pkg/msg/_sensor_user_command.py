# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from sensor_pkg/sensor_user_command.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class sensor_user_command(genpy.Message):
  _md5sum = "07453c0ab726c6f2c228b4f0e11711ec"
  _type = "sensor_pkg/sensor_user_command"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """bool calibrate
bool setepoch
string epoch_sec
string epoch_msec
bool diagnosis_request
bool set_frequency
int8 frequency
bool raw_string
string raw
"""
  __slots__ = ['calibrate','setepoch','epoch_sec','epoch_msec','diagnosis_request','set_frequency','frequency','raw_string','raw']
  _slot_types = ['bool','bool','string','string','bool','bool','int8','bool','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       calibrate,setepoch,epoch_sec,epoch_msec,diagnosis_request,set_frequency,frequency,raw_string,raw

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(sensor_user_command, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.calibrate is None:
        self.calibrate = False
      if self.setepoch is None:
        self.setepoch = False
      if self.epoch_sec is None:
        self.epoch_sec = ''
      if self.epoch_msec is None:
        self.epoch_msec = ''
      if self.diagnosis_request is None:
        self.diagnosis_request = False
      if self.set_frequency is None:
        self.set_frequency = False
      if self.frequency is None:
        self.frequency = 0
      if self.raw_string is None:
        self.raw_string = False
      if self.raw is None:
        self.raw = ''
    else:
      self.calibrate = False
      self.setepoch = False
      self.epoch_sec = ''
      self.epoch_msec = ''
      self.diagnosis_request = False
      self.set_frequency = False
      self.frequency = 0
      self.raw_string = False
      self.raw = ''

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_2B().pack(_x.calibrate, _x.setepoch))
      _x = self.epoch_sec
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.epoch_msec
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2BbB().pack(_x.diagnosis_request, _x.set_frequency, _x.frequency, _x.raw_string))
      _x = self.raw
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 2
      (_x.calibrate, _x.setepoch,) = _get_struct_2B().unpack(str[start:end])
      self.calibrate = bool(self.calibrate)
      self.setepoch = bool(self.setepoch)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.epoch_sec = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.epoch_sec = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.epoch_msec = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.epoch_msec = str[start:end]
      _x = self
      start = end
      end += 4
      (_x.diagnosis_request, _x.set_frequency, _x.frequency, _x.raw_string,) = _get_struct_2BbB().unpack(str[start:end])
      self.diagnosis_request = bool(self.diagnosis_request)
      self.set_frequency = bool(self.set_frequency)
      self.raw_string = bool(self.raw_string)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.raw = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.raw = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_2B().pack(_x.calibrate, _x.setepoch))
      _x = self.epoch_sec
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.epoch_msec
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2BbB().pack(_x.diagnosis_request, _x.set_frequency, _x.frequency, _x.raw_string))
      _x = self.raw
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 2
      (_x.calibrate, _x.setepoch,) = _get_struct_2B().unpack(str[start:end])
      self.calibrate = bool(self.calibrate)
      self.setepoch = bool(self.setepoch)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.epoch_sec = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.epoch_sec = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.epoch_msec = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.epoch_msec = str[start:end]
      _x = self
      start = end
      end += 4
      (_x.diagnosis_request, _x.set_frequency, _x.frequency, _x.raw_string,) = _get_struct_2BbB().unpack(str[start:end])
      self.diagnosis_request = bool(self.diagnosis_request)
      self.set_frequency = bool(self.set_frequency)
      self.raw_string = bool(self.raw_string)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.raw = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.raw = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2B = None
def _get_struct_2B():
    global _struct_2B
    if _struct_2B is None:
        _struct_2B = struct.Struct("<2B")
    return _struct_2B
_struct_2BbB = None
def _get_struct_2BbB():
    global _struct_2BbB
    if _struct_2BbB is None:
        _struct_2BbB = struct.Struct("<2BbB")
    return _struct_2BbB
