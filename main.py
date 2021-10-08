import os
from documents import Document

	
def main():


	bmr_y_pos = 908
	bmr_x_pos = 420
	bmr_file_in = "files/bmr.jpg"
	bmr_file_out = "finals/bmrFinale.jpg"
	bmr = Document(bmr_file_in, bmr_file_out)
	bmr.signDocs(bmr_x_pos, bmr_y_pos)

	swor_front_y = 930
	swor_front_x = 1015
	west_front_file_in = "files/west_swor_front.jpg"
	west_front_file_out = "finals/west_swor_frontFinale.jpg"
	west_front = Document(west_front_file_in, west_front_file_out)
	west_front.signDocs(swor_front_x, swor_front_y)

	swor_back_y = 938
	swor_back_x = 1000
	west_back_file_in = "files/west_swor_back.jpg"
	west_back_file_out = "finals/west_swor_backFinale.jpg"
	west_back = Document(west_back_file_in, west_back_file_out)
	west_back.signDocs(swor_back_x, swor_back_y)


if __name__ == '__main__':
	main()