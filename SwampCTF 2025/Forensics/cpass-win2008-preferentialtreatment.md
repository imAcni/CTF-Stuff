In the pcap file, we find windows 2008 instance and a cpassword:
```                                                        
                                                         cpassword="d
0200   41 77 37 56 51 76 66 6a 39 72 73 35 33 41 38 74   Aw7VQvfj9rs53A8t
0210   34 50 75 64 54 56 66 38 35 43 61 35 63 6d 43 31   4PudTVf85Ca5cmC1
0220   58 6a 78 36 54 70 49 2f 63 53 38 57 44 34 44 38   Xjx6TpI/cS8WD4D8
0230   44 58 62 4b 69 57 49 5a 73 6c 69 68 64 4a 77 33   DXbKiWIZslihdJw3
0240   52 66 2b 69 6a 62 6f 58 37 46 67 4c 57 37 70 46   Rf+ijboX7FgLW7pF
0250   30 4b 36 78 37 64 66 68 51 38 67 78 4c 71 33 34   0K6x7dfhQ8gxLq34
0260   45 4e 47 6a 4e 38 65 54 4f 49 3d 22 0a 20 20 20   ENGjN8eTOI=".   
02
```

Using gpp-decrypt
https://github.com/t0thkr1s/gpp-decrypt
```
gpp-decrypt cpassword
```