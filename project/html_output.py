
class Outputer:

    def __init__(self):
        self.data = []

    def collect_data(self, data):
        if data is None:
            return
        self.data.append(data)

    def output(self):
        file = open('output.html', 'w', encoding='utf-8')

        file.write('<html>')
        file.write('<body>')
        file.write('<table>')

        for d in self.data:
            file.write('<tr>')
            # file.write('<td>%s</td>' % d['url'])
            try:
                file.write('<td>%s</td>' % d['title'])
                print(d['title'])
                file.write('<td>%s</td>' % d['summary'])
                file.write('</tr>')
            except:
                file.write('</tr>')

        file.write('</table>')
        file.write('</body>')
        file.write('</html>')

