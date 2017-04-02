import pdfkit
# https://wkhtmltopdf.org/downloads.html
# https://pypi.python.org/pypi/pdfkit
# http://stackoverflow.com/questions/23359083/how-to-convert-webpage-into-pdf-by-using-python
#cd 'F:\Uni_ETH\0_QBI\Quantitative-Big-Imaging-2017\Lectures'

# baseurl = 'https://rawgit.com/kmader/Quantitative-Big-Imaging-2017/master/Lectures/03-Slides.html#/'
totNoSlides = 60
for i in range(totNoSlides-1):
	fileIn = 'https://rawgit.com/kmader/Quantitative-Big-Imaging-2017/master/Lectures/03-Slides.html#/{0}'.format(i+1)
	fileOut = 'Lecture4_{0}.pdf'.format(i+1)
	pdfkit.from_url(fileIn, fileOut)