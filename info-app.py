
from pywebio.input import *
from pywebio.output import *
from pywebio import start_server


def app():

	put_markdown('# Professional Info')

	#group all the inputs to make a form
	data = input_group("Basic info",[
	    input('Input your name', name='name', required=True),
	    checkbox("Languages of choice", ['JAVA', 'Python', 'C', 'C++'], name='loc'),
	    select("Experience", ['0 - 1', '1 - 2', '2+'], name='yoe', required=True),
	    radio("Gender", options=['Male', 'Female', 'Other'],name='gndr', required=True),
	    textarea('Tell something about yourself', rows=3, name='abt', required=True),
	    file_upload('Profile Image',placeholder='Choose file',accept='image/*',name='dp', required=True)
	])

	#extracting image from input
	img = data['dp']
	with open('img.png', 'wb') as file:
		file.write(img['content'])

	#display image
	put_image(img['content'])

	put_markdown("____")

	# making a list of chosen languages
	loc = "<ul>"
	for i in data['loc']:
		loc += '<li>' + i + '</li>'
	loc += '</ul>'

	# formatting the data with html
	res = f"""
<b>Name:</b> {data['name']}<br>
<b>Languages of choice:</b> {loc}<br>
<b>Experience:</b> {data['yoe']}<br>
<b>Gender:</b> {data['gndr']}<br>
<b>About:</b> {data['abt']}<br>"""

	# displaying the data
	put_html(res)
	
# main function
if __name__ == '__main__':
	start_server(app, port=8585, debug=True)