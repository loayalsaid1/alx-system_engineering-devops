BEGIN {
    FS = ","
    males = 0
    females = 0
}

{
    if ( $4 == "M" ) {
        males++
    } else {
        females++
    }
}

END {
    print "Male emploees coutn => " males
    print "Female employess count => " females
}  
