BEGIN {
    basename = ARGV[1]
    printf("    def %s(self):\n", basename)
    printf("        checkFileName = '%s' + '.good'\n", basename)
    printf("        outFileName = '%s' + '.out'\n\n", basename)
    printf("        with open(outFileName, 'w') as outf:\n")
    printf("            with redirect_stdout(outf):\n")

    while (getline line < (basename ".py") > 0) 
        if (line !~ /^from/)
            print "                " line 

    print "        with open(outFileName) as outf:"
    print "            outStr = outf.read()"
    print "        with open(checkFileName) as f:"
    print "            checkStr = f.read()"
    print
    print "        self.assertEqual(outStr, checkStr)"
}
