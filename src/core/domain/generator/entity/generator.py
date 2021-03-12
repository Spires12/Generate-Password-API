import attr


@attr.s(auto_attribs=True)
class Generator():
  """ Base generator entity """
  
  length_password: int = 0
  include_symbols: bool = False
  include_numbers: bool = False
  include_lowercase_letters: bool = False
  include_uppercase_characters: bool = False

