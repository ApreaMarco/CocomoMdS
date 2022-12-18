LANGS = {
  'python': {
  'estensioni': ['py'],
  'keywords': [
    'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 
    'continue', 'def', 'del', 'elif', 'else', 'except', 'finally',  'for', 'from', 'global',
    'if', 'import',  'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
    'try', 'while', 'with', 'yield'],
  'contatore' : 0
  },

  'java': {
  'estensioni': ['java'],
  'keywords': [
    'abstract', 'continue', 'for', 'new', 'switch', 'assert', 'default', 'goto', 'package',
    'synchronized', 'boolean', 'do', 'if', 'private', 'this', 'break', 'double', 'implements',
    'protected', 'throw', 'byte', 'else', 'import', 'public', 'throws', 'case', 'enum', 
    'instanceof', 'return', 'transient', 'catch', 'extends', 'int', 'short', 'try', 'char', 
    'final', 'interface', 'static', 'void', 'class', 'finally', 'long', 'strictfp', 'volatile',
    'const', 'float', 'native', 'super', 'while'],
  'contatore' : 0
  },

  'javascript': {
  'estensioni': ['js'],
  'keywords': [
    'break', 'case', 'catch', 'class', 'const', 'continue', 'debugger', 'default', 'package',
    'delete', 'do', 'else', 'export', 'extends', 'finally', 'for', 'function', 'if', 'try',
    'import', 'in', 'instanceof', 'new', 'return', 'super', 'switch', 'this', 'throw', 
    'var', 'void', 'while', 'with', 'yield', 'enum', 'implements', 'interface', 'let',
    'private', 'protected', 'public', 'static', 'await', 'null', 'true', 'false'],
  'contatore' : 0
  },

  'c': {
  'estensioni': ['c'],
  'keywords': [
    'auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do', 'double', 'unsigned',
    'else', 'enum', 'extern', 'float', 'for', 'goto', 'if', 'inline', 'int', 'long', 'register', 
    'return', 'short', 'signed', 'sizeof', 'static', 'struct', 'switch', 'typedef', 'union', 
    'void', 'volatile', 'while'],
  'contatore' : 0
  },

  'c++': {
  'estensioni': ['cpp'],
  'keywords': [
    'alignas', 'alignof', 'and', 'and_eq', 'asm', 'atomic_cancel', 'atomic_commit', 'atomic_noexcept',
    'auto', 'bitand', 'bitor', 'bool', 'break', 'case', 'catch', 'char', 'char8_t', 'char16_t', 'char32_t',
    'class', 'concept', 'const', 'consteval', 'constexpr', 'constinit', 'const_cast', 'continue', 'co_await',
    'co_return', 'co_yield', 'decltype', 'default', 'delete', 'do', 'double', 'dynamic_cast', 'else', 'enum',
    'explicit', 'export', 'extern', 'false', 'float', 'for', 'friend', 'goto', 'if', 'import', 'inline', 'int',
    'long', 'module', 'mutable', 'namespace', 'new', 'noexcept', 'not', 'not_eq', 'nullptr', 'operator', 'or',
    'or_eq', 'private', 'protected', 'public', 'reflexpr', 'register', 'reinterpret_cast', 'requires', 'return',
    'short', 'signed', 'sizeof', 'static', 'static_assert', 'static_cast', 'struct', 'switch', 'synchronized', 
    'template', 'this', 'thread_local', 'throw', 'true', 'try', 'typedef', 'typeid', 'typename', 'union', 
    'unsigned', 'using', 'virtual', 'void', 'volatile', 'wchar_t', 'while', 'xor', 'xor_eq'],
  'contatore' : 0
  },

  'c#': {
  'estensioni': ['cs'],
  'keywords': [
    'abstract', 'as', 'base', 'bool', 'break', 'byte', 'case', 'catch', 'char', 'checked', 'class', 'const', 
    'continue', 'decimal', 'default', 'delegate', 'do', 'double', 'else', 'enum', 'event', 'explicit', 'extern',
    'false', 'finally', 'fixed', 'float', 'for', 'foreach', 'goto', 'if', 'implicit', 'in', 'int', 'interface', 
    'internal', 'is', 'lock', 'long', 'namespace', 'new', 'null', 'object', 'operator', 'out', 'override',
    'params', 'private', 'protected', 'public', 'readonly', 'ref', 'return', 'sbyte', 'sealed', 'short', 'sizeof',
    'stackalloc', 'static', 'string', 'struct', 'switch', 'this', 'throw', 'true', 'try', 'typeof', 'uint', 'ulong',
    'unchecked', 'unsafe', 'ushort', 'using', 'virtual', 'void', 'volatile', 'while'],
  'contatore' : 0
  },
  
  'php': {
  'estensioni': ['php'],
  'keywords': [
    'and', 'or', 'xor', 'array', 'as', 'break', 'case', 'class', 'const', 'continue', 'declare', 'default', 'die',
    'do', 'echo', 'else', 'elseif', 'empty', 'enddeclare', 'endfor', 'endforeach', 'endif', 'endswitch', 'endwhile',
    'eval', 'exit', 'extends', 'false', 'for', 'foreach', 'function', 'global', 'if', 'include', 'include_once', 
    'isset', 'list', 'new', 'null', 'print', 'require', 'require_once', 'return', 'static', 'switch', 'true', 'unset',
    'use', 'var', 'while', '__class__', '__dir__', '__file__', '__function__', '__method__', '__namespace__', 'final',
    'php_user_filter', 'interface', 'implements', 'extends', 'public', 'private', 'protected', 'abstract', 'clone', 
    'try', 'catch', 'throw', 'calls', 'parent', 'self'],
  'contatore' : 0
  },

  'assembly': {
  'estensioni': ['asm'],
  'keywords': [
    'mov', 'add', 'sub', 'mul', 'div', 'inc', 'dec', 'jmp', 'je', 'jne', 'jg', 'jl', 'call', 'ret', 'int', 'push', 
    'pop', 'cmp', 'and', 'or', 'xor', 'not', 'neg', 'shl', 'shr', 'rol', 'ror', 'nop', 'hlt', 'iret'],
  'contatore' : 0
  },

  'batch': {
  'estensioni': ['bat'],
  'keywords': [
    'echo', 'date', 'time', 'dir', 'cd', 'copy', 'xcopy', 'del', 'md', 'rd', 'type', 'ren', 'sort', 'find', 'for', 
    'if', 'goto', 'call', 'start', 'set', 'rem'],
  'contatore' : 0
  },

  'bash': {
  'estensioni': ['bash'],
  'keywords': ['if', 'then', 'else', 'elif', 'fi', 'case', 'esac', 'for', 'select', 'while', 'until', 'do', 'done', 
  'in', 'function', 'time', '{', '}', '[', ']'],
  'contatore' : 0
  },

  'powershell': {
  'estensioni': ['ps1'],
  'keywords': [
    'if', 'else', 'elseif', 'switch', 'for', 'foreach', 'while', 'do', 'break', 'continue', 'return', 'try', 'catch',
    'finally', 'throw', 'function', 'filter', 'begin', 'process', 'param', 'class', 'static', '$true', '$false', '$null'],
  'contatore' : 0
  },

  'ruby': {
  'estensioni': ['rb'],
  'keywords': [
    'class', 'def', 'begin', 'end', 'if', 'else', 'elsif', 'unless', 'case', 'when', 'while', 'until', 'for', 'break', 
    'next', 'redo', 'retry', 'in', 'do', 'return', 'yield', 'self', 'super', 'alias', 'public', 'protected', 'private', 
    'const', 'static', 'var', 'let', 'set', 'get', 'willSet', 'didSet'],
  'contatore' : 0
  },
  
  'go': {
  'estensioni': ['go'],
  'keywords': [
    'func', 'typealias', 'associatedtype', 'struct', 'enum', 'protocol', 'extension', 'import', 'guard', 'switch', 
    'where', 'break', 'continue', 'fallthrough', 'return', 'inout', 'mutating', 'nonmutating', '__COLUMN__', 
    '__FILE__', '__FUNCTION__', '__LINE__'],
  'contatore' : 0
  },

  'swift': {
  'estensioni': ['swift'],
  'keywords': [
    'associatedtype', 'class', 'deinit', 'enum', 'extension', 'fileprivate', 'func', 'import', 'init', 'inout', 
    'internal', 'let', 'open', 'operator', 'private', 'protocol', 'public', 'static', 'struct', 'subscript', 
    'typealias', 'var', 'break', 'case', 'continue', 'default', 'defer', 'do', 'else', 'fallthrough', 'for', 'guard',
    'if', 'in', 'repeat', 'return', 'switch', 'where', 'while', 'as', 'Any', 'catch', 'false', 'is', 'nil', 'rethrows',
    'super', 'self', 'Self', 'throw', 'throws', 'true', 'try', '#available', '#colorLiteral', '#column', '#else', 
    '#elseif', '#endif', '#file', '#fileLiteral', '#function', '#if', '#imageLiteral', '#line', '#selector', 
    '#sourceLocation', '#warning', '#error'],
  'contatore' : 0
  },
}