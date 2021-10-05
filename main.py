import os
from documents import Document

	
def main():

	bmr_sig_width = 170
	bmr_sig_height = 30
	bmr_y_pos = 908
	bmr_x_pos = 420
	bmr_file_in = "files/bmr.jpg"
	bmr_file_out = "finals/bmrFinale.jpg"
	bmr = Document(bmr_file_in, bmr_file_out)
	bmr.signatureSize(bmr_sig_width, bmr_sig_height)
	bmr.signDocs(bmr_x_pos, bmr_y_pos)


if __name__ == '__main__':
	main()