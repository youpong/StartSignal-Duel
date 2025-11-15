# DEVELOPMENT
MicroPython aims to implement Python 3.4 standard (with selected features from
later versions). Furthermore, BBC micro:bit MicroPython, which is derived from
it, has additional limitations due to reduced memory usage and other 
constraints. This section lists the features that could not be used and the
alternative features used (if any).

* f-strings are not supported on BBC micro:bit MicroPython; using format()
  instead.
* The walrus operator (:=) is not supported on MicroPython.
