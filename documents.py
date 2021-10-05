from PIL import Image

class Document:
	file = ' '
	file_out = ' '
	sig_width = 170
	sig_height = 30
	def __init__(self, file, file_out):
		self.file = file
		self.file_out = file_out
	

	def signDocs(self, x_pos, y_pos):

		signature = Image.open("files/barry_signature_clean.jpg")
		newsize = (self.sig_width, self.sig_height)
		img1 = signature.resize(newsize)
		img2 = Image.open(self.file)
		area = (x_pos, y_pos, (x_pos + self.sig_width), (y_pos + self.sig_height))
		img2.paste(img1, area)
		print(f'img1 format: {signature.format} img1 size: {signature.size}')
		print(f'img2 format: {img2.format} img2 size:{img2.size}')

		print(f'signature size {img1.size}')
		img2.save(self.file_out, "JPEG")
		print('Saved')