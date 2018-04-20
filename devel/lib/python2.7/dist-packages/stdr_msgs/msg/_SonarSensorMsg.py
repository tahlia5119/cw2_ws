# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from stdr_msgs/SonarSensorMsg.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import stdr_msgs.msg
import geometry_msgs.msg

class SonarSensorMsg(genpy.Message):
  _md5sum = "e8b8bd75b2e357572ea0c9ee72ed58c1"
  _type = "stdr_msgs/SonarSensorMsg"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# Rfid sensor description
float32 maxRange
float32 minRange
float32 coneAngle

float32 frequency
stdr_msgs/Noise noise

string frame_id
geometry_msgs/Pose2D pose # sensor pose, relative to robot center

================================================================================
MSG: stdr_msgs/Noise
bool noise
float32 noiseMean
float32 noiseStd

================================================================================
MSG: geometry_msgs/Pose2D
# This expresses a position and orientation on a 2D manifold.

float64 x
float64 y
float64 theta"""
  __slots__ = ['maxRange','minRange','coneAngle','frequency','noise','frame_id','pose']
  _slot_types = ['float32','float32','float32','float32','stdr_msgs/Noise','string','geometry_msgs/Pose2D']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       maxRange,minRange,coneAngle,frequency,noise,frame_id,pose

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SonarSensorMsg, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.maxRange is None:
        self.maxRange = 0.
      if self.minRange is None:
        self.minRange = 0.
      if self.coneAngle is None:
        self.coneAngle = 0.
      if self.frequency is None:
        self.frequency = 0.
      if self.noise is None:
        self.noise = stdr_msgs.msg.Noise()
      if self.frame_id is None:
        self.frame_id = ''
      if self.pose is None:
        self.pose = geometry_msgs.msg.Pose2D()
    else:
      self.maxRange = 0.
      self.minRange = 0.
      self.coneAngle = 0.
      self.frequency = 0.
      self.noise = stdr_msgs.msg.Noise()
      self.frame_id = ''
      self.pose = geometry_msgs.msg.Pose2D()

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
      buff.write(_get_struct_4fB2f().pack(_x.maxRange, _x.minRange, _x.coneAngle, _x.frequency, _x.noise.noise, _x.noise.noiseMean, _x.noise.noiseStd))
      _x = self.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_3d().pack(_x.pose.x, _x.pose.y, _x.pose.theta))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.noise is None:
        self.noise = stdr_msgs.msg.Noise()
      if self.pose is None:
        self.pose = geometry_msgs.msg.Pose2D()
      end = 0
      _x = self
      start = end
      end += 25
      (_x.maxRange, _x.minRange, _x.coneAngle, _x.frequency, _x.noise.noise, _x.noise.noiseMean, _x.noise.noiseStd,) = _get_struct_4fB2f().unpack(str[start:end])
      self.noise.noise = bool(self.noise.noise)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.frame_id = str[start:end].decode('utf-8')
      else:
        self.frame_id = str[start:end]
      _x = self
      start = end
      end += 24
      (_x.pose.x, _x.pose.y, _x.pose.theta,) = _get_struct_3d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_4fB2f().pack(_x.maxRange, _x.minRange, _x.coneAngle, _x.frequency, _x.noise.noise, _x.noise.noiseMean, _x.noise.noiseStd))
      _x = self.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_3d().pack(_x.pose.x, _x.pose.y, _x.pose.theta))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.noise is None:
        self.noise = stdr_msgs.msg.Noise()
      if self.pose is None:
        self.pose = geometry_msgs.msg.Pose2D()
      end = 0
      _x = self
      start = end
      end += 25
      (_x.maxRange, _x.minRange, _x.coneAngle, _x.frequency, _x.noise.noise, _x.noise.noiseMean, _x.noise.noiseStd,) = _get_struct_4fB2f().unpack(str[start:end])
      self.noise.noise = bool(self.noise.noise)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.frame_id = str[start:end].decode('utf-8')
      else:
        self.frame_id = str[start:end]
      _x = self
      start = end
      end += 24
      (_x.pose.x, _x.pose.y, _x.pose.theta,) = _get_struct_3d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_4fB2f = None
def _get_struct_4fB2f():
    global _struct_4fB2f
    if _struct_4fB2f is None:
        _struct_4fB2f = struct.Struct("<4fB2f")
    return _struct_4fB2f
_struct_3d = None
def _get_struct_3d():
    global _struct_3d
    if _struct_3d is None:
        _struct_3d = struct.Struct("<3d")
    return _struct_3d
