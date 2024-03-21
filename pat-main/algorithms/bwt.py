# Note that the "$" character will be used to designate the end of a given
# string.


def solve_bwt():
    """Load the mystery.txt file and decode its contents using the
    reverse BWT transformation. Report the decoded contents."""

    # Example sequences for forward_bwt() and reverse_bwt();
    # you may change them to different sequences to test your code.
    """
    seq1 = "GATTACA$"
    seq2 = "ACTGA$TA"
    forward_bwt(seq1)
    reverse_bwt(seq2)
    """

    # Code to open the file mystery.txt in the correct encoding
    # across platforms, and read its contents into a variable.
    """
    with open("mystery.txt", "r", encoding="UTF-8") as f:
        mystery_seq = f.read()
    """
    #
    # YOUR CODE GOES HERE
    #

    # TESTS:
    # print("forward_bwt tests")
    # print(forward_bwt("AGGCTGCA$"))
    # print(forward_bwt("GACCTA$"))
    # print("\n")
    #
    # print("reverse_bwt tests")
    # print(reverse_bwt("AC$GGTGAC"))
    # print(reverse_bwt("ATGAC$C"))
    # print("\n")

    # REPORT 1:
    report1 = forward_bwt("GGACTAACGGACTAACGGACTAACGGACTAC$")
    print("The result of the BWT applied to GGACTAACGGACTAACGGACTAACGGACTAC$ is " + report1)
    print("\n")

    # REPORT 2:
    temp_report2 = "ntydmdeedneetnehngdersrneed_-eghseedldter-_$__________..r...m.....snnne,eroystsg,ge,,rnee,toogwes,,,teeetteo,etsededtooeedrdfyedegedtsrtar,esrertofhtteetaaestle,teyddeyotedeed,ddettttdaenltre,nrlelenwtstynaao,lleehndtt,,doeeeetrarde,skgylerrd,d,endroet,nofdrt,efrmoesfyrooetmthhontrer,sendde,errenltw,,tttdtrgrkye,dden________lreee__g_rmvtunh_hhh_hccv______ccc_wwff___lee_etlehehehhhhhehhhhhhhhcccecrccrrrfnnnnnbchhhhrgghs____mi_oaA_________iiiiii_annnii_n______seen_aeleoaenneneleeieeeeeldnnanneealea_________n___eeeeee___enarllrtltslvrrvtrwWhwwwvvrsbrvhrcsrrhWrbwrskhhvrlrvhhhhwwwvvvvmrhrshdddy_rmrrrrssvtcrstltgvittthdddddderbhcciirmrmmv__snmppp_hdhhvghpwbhhhhhhhhhpvhbvhhrrtmgghdsnddnnhhhtooooo____-_n______e_______nnnnnnnnn__arrouiuuiga_____ttstccsss_atttttttttwtttwt_____TtttttttttTsttttt_________tttwtttww_ttttgwww_tsgggtlddddddhhddffhmvw____fL_tvtvtntafatttttttttebh_h_hh_rn__sflleelcllsraallllllaip__euerpppttg______aiuaaaao__laobhoaooeeo_e__n__loeoooiieiaoaoooooiei_____aooiiuaaaaaauei___uiiiiiooieiiraaa__onnn___eooeeoaiotttstshhsghttttdnG_____tcsdrrciii_iiii_iccllhcccipreeer__nofffffcfnfwwfphpnnnnnnvvrfhr__FbgNpl___o_-ooo__o___eaeaeaooueeeiououeaeeooeooeotbcc__beeeuoaeaeeeeaueocgggcof____aoeooeffppbgaeoaioeteiaririuiiiiuu__neueonna__i___i_oa___eaee_aunucaaiaaooiahasaoohIIIuhaaneoaaaaaaaaae__oaaaaaaaa_arrr___—_____—_—___________aeaea_______—___nstsaaaaraioott________lesiairqrooofo__ooodsh__a_Bb_diaaaaaolaaaiieeoiiiieeeeo_____—____o___________otleaenlbe_snnwe"
    temp_report2 = reverse_bwt(temp_report2)
    report2 = ""

    for char in temp_report2:  # replacing _ with spaces
        if char == "_":
            report2 += " "
        else:
            report2 += char

    print("The encoded message is as follows:")
    print(report2)

def forward_bwt(seq):
    """forward_bwt(seq) takes as input a string containing the EOF character to
    which the BWT must be applied. The method should then return the result of
    the BWT on the input string.

    For example:
        forward_bwt("GATTACA$") --> "ACTGA$TA"

    Args:
        seq (str): input string with an EOF character

    Returns:
        (str): the transformed string
    """

    # STEP 1: Create array of cyclic permutations!
    BWT_string = ""  # string to hold the result of the BWT
    BWM = []  # array to hold the cyclic permutations
    for i in range(len(seq)):
        BWM.append(seq[i:] + seq[:i])  # ter

    # STEP 2: Sort alphabetically!
    sorted_BWM = sorted(BWM)

    # STEP 3: Select last letter from every item in array!
    for item in sorted_BWM:
        BWT_string += item[-1] # last letter

    return BWT_string

def reverse_bwt(seq):
    """reverse_bwt(seq) takes as input a string containing the EOF character to
    which the reverse of the BWT must be applied. The method should then return
    the result of the reversal on the input string.

    For example:
        reverse_bwt("ACTGA$TA") --> "GATTACA$"

    Args:
        seq (str): input string with an EOF character

    Returns:
        (str): the transformed string
    """
    # General process of sort + append:
    # STEP 1: Sort alphabetically
    # STEP 2: Append the seq (aka the temp first column of the BWM)
    # STEP 3: Repeat STEP 1 and 2 until we reach the desired length (len of seq)

    og_string = ""
    length = len(seq)  # this is the length we want to reach
    BWM = [""] * length  # list of empty strings

    for i in range(length):  # reconstructing BWM
        temp_BWM = []  # holds temp_BWM aka appended creation
        for j in range(length):
            temp_BWM.append(seq[j] + BWM[j])  # append
        BWM = sorted(temp_BWM)  # sort

    for item in BWM:  # selecting row with $ marker at end aka og string
        if item[-1] == "$":
            og_string = item

    return og_string

if __name__ == "__main__":
    """Run solve_bwt(). Do not modify this code"""
    solve_bwt()
