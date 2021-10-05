import os
from documents import Document

	
def main():


	bmr_y_pos = 908
	bmr_x_pos = 420
	bmr_file_in = "files/bmr.jpg"
	bmr_file_out = "finals/bmrFinale.jpg"
	bmr = Document(bmr_file_in, bmr_file_out)
	bmr.signDocs(bmr_x_pos, bmr_y_pos)

	west_front_y = 930
	west_front_x = 1015
	west_front_file_in = "files/west_swor_front.jpg"
	west_front_file_out = "finals/west_swor_frontFinale.jpg"
	west_front = Document(west_front_file_in, west_front_file_out)
	west_front.signDocs(west_front_x, west_front_y)


if __name__ == '__main__':
	main()