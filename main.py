import os
from documents import Document

	
def main():


	try:
		bmr_y_pos = 908
		bmr_x_pos = 420
		bmr_file_in = "files/bmr.jpg"
		bmr_file_out = "finals/bmrFinale.jpg"
		bmr = Document(bmr_file_in, bmr_file_out)
		bmr.signDocs(bmr_x_pos, bmr_y_pos)
	except:
		print('Trouble opening BMR')

	try:
		swor_front_y = 930
		swor_front_x = 1015
		west_front_file_in = "files/west_swor_front.jpg"
		west_front_file_out = "finals/west_swor_frontFinale.jpg"
		west_front = Document(west_front_file_in, west_front_file_out)
		west_front.signDocs(swor_front_x, swor_front_y)
	except:
		print('Trouble opening West Surface Water Front')

	try:
		swor_back_y = 938
		swor_back_x = 1000
		west_back_file_in = "files/west_swor_back.jpg"
		west_back_file_out = "finals/west_swor_backFinale.jpg"
		west_back = Document(west_back_file_in, west_back_file_out)
		west_back.signDocs(swor_back_x, swor_back_y)
	except:
		print('Trouble opening West Surface Back')

	try:
		swor_front_y = 930
		swor_front_x = 1015
		west_front_file_in = "files/east_swor_front.jpg"
		west_front_file_out = "finals/east_swor_frontFinale.jpg"
		west_front = Document(west_front_file_in, west_front_file_out)
		west_front.signDocs(swor_front_x, swor_front_y)
	except:
		print('Trouble opening East Surface Water Front')

	try:
		swor_back_y = 938
		swor_back_x = 1000
		west_back_file_in = "files/east_swor_back.jpg"
		west_back_file_out = "finals/east_swor_backFinale.jpg"
		west_back = Document(west_back_file_in, west_back_file_out)
		west_back.signDocs(swor_back_x, swor_back_y)
	except:
		print('Trouble opening East Surface Water back')

	try:
		ifmr_y = 945
		ifmr_x = 170
		west_ifmr_first = "files/west_ifmr_page_one.jpg"
		west_ifmr_first_out = "finals/west_ifmr_page_oneFinale.jpg"
		w_ifmr_first = Document(west_ifmr_first, west_ifmr_first_out)
		w_ifmr_first.signDocs(ifmr_x, ifmr_y)
	except:
		print('Trouble opening first page of West IFMR')
	try:
		ifmr_two_y = 820
		ifmr_two_x = 170
		west_ifmr_second = "files/west_ifmr_page_two.jpg"
		west_ifmr_second_out = "finals/west_ifmr_page_twoFinale.jpg"
		w_ifmr_first = Document(west_ifmr_second, west_ifmr_second_out)
		w_ifmr_first.signDocs(ifmr_two_x, ifmr_two_y)
	except:
		print('Trouble opening second page of West IFMR')

	try:
		ifmr_y = 945
		ifmr_x = 170
		east_ifmr_first = "files/east_ifmr_page_one.jpg"
		east_ifmr_first_out = "finals/east_ifmr_page_oneFinale.jpg"
		e_ifmr_first = Document(east_ifmr_first, east_ifmr_first_out)
		e_ifmr_first.signDocs(ifmr_x, ifmr_y)
	except:
		print('Trouble opening first page of East IFMR')

	try:
		ifmr_two_y = 820
		ifmr_two_x = 170
		east_ifmr_second = "files/east_ifmr_page_two.jpg"
		east_ifmr_second_out = "finals/east_ifmr_page_twoFinale.jpg"
		e_ifmr_second = Document(east_ifmr_second, east_ifmr_second_out)
		e_ifmr_second.signDocs(ifmr_two_x, ifmr_two_y)
	except:
		print('Trouble opening second page of East IFMR')
if __name__ == '__main__':
	main()