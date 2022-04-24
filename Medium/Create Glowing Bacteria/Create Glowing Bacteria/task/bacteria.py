file_name = input()
file_data = open(file_name)

original_plasmid_strand = file_data.readline().strip()
original_plasmid_restriction_site = file_data.readline().strip()
original_GFP_strand = file_data.readline().strip()
first_restriction_site_GFP, second_restriction_site_GFP = file_data.readline().split()


def get_complementary_strand(original_strand):
    complementary_bases = {"A": "T",
                           "G": "C",
                           "T": "A",
                           "C": "G"}
    complementary_strand = ""
    for base in original_strand:
        complementary_strand += complementary_bases[base]
    return complementary_strand


def cut_plasmid(plasmid_strand, restriction_site):
    complementary_strand = get_complementary_strand(plasmid_strand)
    complementary_restriction_site = get_complementary_strand(restriction_site)

    original_restriction_index = plasmid_strand.find(restriction_site) + 1
    complementary_restriction_index = complementary_strand.find(complementary_restriction_site) + 5

    return [plasmid_strand[0:original_restriction_index], plasmid_strand[original_restriction_index:],
            complementary_strand[0:complementary_restriction_index], complementary_strand[complementary_restriction_index:]]



def cut_GFP(original_strand, restriction_site_1, restriction_site_2):

    GFP_complementary = get_complementary_strand(original_strand)

    complementary_restriction_site_1 = get_complementary_strand(restriction_site_1)

    complementary_restriction_site_2 = get_complementary_strand(restriction_site_2)

    original_restriction_left = original_strand.find(restriction_site_1) + 1
    original_restriction_right = original_strand.rfind(restriction_site_2) + 1

    complementary_restriction_left = GFP_complementary.find(complementary_restriction_site_1) + 5
    complementary_restriction_right = GFP_complementary.rfind(complementary_restriction_site_2) + 5

    GFP_original_cut = original_strand[original_restriction_left:original_restriction_right]
    GFP_complementary_cut = GFP_complementary[complementary_restriction_left:complementary_restriction_right]

    return [GFP_original_cut, GFP_complementary_cut]


def ligation(plasmid_data: list, GFP_data: list):
    original_strand = plasmid_data[0] + GFP_data[0] + plasmid_data[1]
    complementary_strand = plasmid_data[2] + GFP_data[1] + plasmid_data[3]
    return original_strand, complementary_strand


plasmid = cut_plasmid(original_plasmid_strand, original_plasmid_restriction_site)
GFP = cut_GFP(original_GFP_strand, first_restriction_site_GFP, second_restriction_site_GFP)
ligated_original, ligated_complementary = ligation(plasmid, GFP)

print(ligated_original)
print(ligated_complementary)
