#!/usr/bin/env python3
# -*- coding: ascii -*-
from __future__ import unicode_literals, division, with_statement

Node = r"""(function(program, execJS) { execJS(program) })(function() { #{source}
}, function(program) {
  var output;
  var print = function(string) {
    process.stdout.write('' + string + '\n');
  };
  try {
    result = program();
    print('')
    if (typeof result == 'undefined' && result !== null) {
      print('["ok"]');
    } else {
      try {
        print(JSON.stringify(['ok', result]));
      } catch (err) {
        print('["err"]');
      }
    }
  } catch (err) {
    print(JSON.stringify(['err', '' + err]));
  }
});"""
