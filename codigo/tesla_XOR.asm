01      pop esi
02      add esi, 0x62
03      lea edi, [esi+0x2CB]
04      imul edx, edx, 0x0
05      imul edx, edx, 0x385B7BD9
06      add edx, 0x68D23EF5
07      xor [esi], edx
08      add esi, 0x4
09      cmp esi, edi
0A      jc 05