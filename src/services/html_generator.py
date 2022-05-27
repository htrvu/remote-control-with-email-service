def html_table(dataframe, format = 'center'):
    '''
        Create HTML table code for `dataframe`, with `format` alignment for columns
        `dataframe` is a dictionary with the following information:
            - `columns`: list of column names
            - `data`: list of tuple with the values corresponding to the column names
    '''
    n_row = len(dataframe['data'])
    n_col = len(dataframe['columns'])

    columns = dataframe['columns']
    data = dataframe['data']

    html = f'<table class="{format}">'

    html += '<tr class="first-row">'
    for column in columns:
        html += f'<th>{column}</th>'
    html += '</tr>'

    for i in range(n_row):
        html += '<tr class="'
        if i % 2 == 1:
            html += 'odd-row'
        if i == n_row:
            html += 'last-row'
        html += '">'

        for j in range(n_col):
            html += f'<td>{data[i][j]}</td>'
        html += '</tr>'

    return html

def html_text():
    pass

def html_image():
    pass

def html_video():
    pass


def html_mail(request, content):
    '''
        Create a HTML mail message which is used to response the request
        `content` is generated by the above functions
    '''

    html_template = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <style>
            * {
                box-sizing: border-box;
            }

            html {
                font-family: 'Roboto', sans-serif;
            }

            p, td, th, span {
                color: #333;
                font-size: 16px;
            }

            .main {
                margin: 0 auto;
                border: 1px solid #ccc;
                border-radius: 10px;
                padding: 6px 30px 30px 30px;
                width: 700px;
            }

            .app__name {
                text-align: center;
                font-size: 24px;
                color: #1e9d95;
                font-weight: bold;
            }

            .app__greeting,
            .app__desc {
                text-align: center;
            }

            .divider {
                border-bottom: 1px solid #ccc;
                margin: 20px 0;
            }

            .request {
                font-weight: bold;
            }

            /* CSS for tables */
            table {
                /* width: 100%; */
                margin: 0 auto;
                border-collapse: collapse;
                overflow: hidden;
            }

            table.left {
                text-align: left;
            }

            table.center {
                text-align: center;
            }

            td,
            th {
                border-top: 1px solid #ecf0f1e6;
                padding: 10px 14px;
            }

            th {
                background-color: #76dfd8;
            }

            td {
                border-left: 1px solid #ecf0f1;
                border-right: 1px solid #ecf0f1;
            }
            
            tr.first-row {
                text-align: center;
            }

            tr.last-row {
                border-bottom: 1px solid #ecf0f1e6;
            }

            tr.odd-row td {
                background-color: #e6f8f7;
            }
        </style>
    </head>
    <body>
        <div class='main'>
            <div class="container">
                <p class="app__name">Remote Control with Email Service</p>
                <p class="app__greeting">Greeting from <span style='font-weight: bold;'>Group 8</span> - Honors Program 2020, University of Science, VNUHCM.</p>
                <p class="app__desc">This is our final project for <span style='font-weight: bold;'>Computer Networking</span> course (CSC10008) and thank you for using our application!</p>
                <div class='divider'></div>
            </div>

            <div class="container">
                <p>This mail responses to the request: <span class="request">''' + request + '''</span></p>
            </div>
    '''

    html_template += f'''
        <section>
            {content}
        </section>
        </div>
        </body>
    </html>
    '''       
    
    return html_template