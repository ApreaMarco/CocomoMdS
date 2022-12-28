# Initialize the costDriver values
costDriver1 = {"ACAP": 1.46,
               "AEXP": 1.29,
               "CPLX": 0.7,
               "DATA": 0,
               "LEXP": 1.14,
               "MCDP": 1.24,
               "PCAP": 0.75,
               "RELY": 1.23,
               "SCED": 1.23,
               "STOR": 0,
               "TIME": 0,
               "TOOL": 1.24,
               "TURN": 0,
               "VEXP": 1.21,
               "VIRT": 0}

costDriver2 = {"ACAP": 1.19,
               "AEXP": 1.13,
               "CPLX": 0.85,
               "DATA": 0.94,
               "LEXP": 1.07,
               "MCDP": 1.1,
               "PCAP": 1.17,
               "RELY": 0.88,
               "SCED": 1.08,
               "STOR": 0,
               "TIME": 0,
               "TOOL": 1.1,
               "TURN": 0.87,
               "VEXP": 1.10,
               "VIRT": 0.87}

costDriver3 = {"ACAP": 1,
               "AEXP": 1,
               "CPLX": 1,
               "DATA": 1,
               "LEXP": 1,
               "MCDP": 1,
               "PCAP": 1,
               "RELY": 1,
               "SCED": 1,
               "STOR": 1,
               "TIME": 1,
               "TOOL": 1,
               "TURN": 1,
               "VEXP": 1,
               "VIRT": 1}

costDriver4 = {"ACAP": 0.86,
               "AEXP": 0.91,
               "CPLX": 1.15,
               "DATA": 1.08,
               "LEXP": 0.95,
               "MCDP": 0.91,
               "PCAP": 0.86,
               "RELY": 1.15,
               "SCED": 1.04,
               "STOR": 1.06,
               "TIME": 1.11,
               "TOOL": 0.91,
               "TURN": 1.07,
               "VEXP": 0.9,
               "VIRT": 1.15}

costDriver5 = {"ACAP": 0.71,
               "AEXP": 0.86,
               "CPLX": 1.3,
               "DATA": 1.16,
               "LEXP": 0,
               "MCDP": 0.82,
               "PCAP": 0.7,
               "RELY": 1.4,
               "SCED": 1.1,
               "STOR": 1.21,
               "TIME": 1.3,
               "TOOL": 0.83,
               "TURN": 1.15,
               "VEXP": 0,
               "VIRT": 1.3}

costDriver6 = {"ACAP": 0,
               "AEXP": 0,
               "CPLX": 1.65,
               "DATA": 0,
               "LEXP": 0,
               "MCDP": 0,
               "PCAP": 0,
               "RELY": 0,
               "SCED": 0,
               "STOR": 1.56,
               "TIME": 1.66,
               "TOOL": 0,
               "TURN": 0,
               "VEXP": 0,
               "VIRT": 0}

# Assign the costDriver
def assignCostDriver(dif):
    if (dif == 1):
        costDriver = costDriver1
    elif (dif == 2):
        costDriver = costDriver2
    elif (dif == 3):
        costDriver = costDriver3
    elif (dif == 4):
        costDriver = costDriver4
    elif (dif == 5):
        costDriver = costDriver5
    elif (dif == 6):
        costDriver = costDriver6
    return costDriver
