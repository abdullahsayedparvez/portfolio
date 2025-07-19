
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Portfolio data
    portfolio_data = {
        'name': 'Abdullah Sayed',
        'tagline': 'Data Engineer | Scalable Pipelines • API Integration • Data Insights',
        'intro': "Hi, I'm a Data Engineer who turns raw data into real impact. With a passion for clean pipelines and meaningful insights, I build data systems that power smarter decisions—especially in finance and business environments.",
        'photo_url': 'https://media.licdn.com/dms/image/v2/D4D03AQEEDkN-8ZthvQ/profile-displayphoto-shrink_400_400/B4DZWlqyGuH4Ag-/0/1742241211458?e=1758153600&v=beta&t=KI5-CsA5LyQwEBiPhu1rAF6vBAVUvRpg2dFNsxM44E8',
        'about': {
            'bio': "I'm a Data Engineer with over a year of hands-on experience designing and implementing robust data solutions. I specialize in building scalable ETL pipelines, automating data workflows, and managing end-to-end data processes. My skill set includes working with relational and non-relational databases, integrating and managing APIs, and ensuring efficient data flow across systems. I'm well-versed in data collection, preprocessing, analysis, and visualization—primarily within financial and business domains. I'm passionate about transforming raw data into actionable insights that drive smarter decision-making.",
            'experience': '1+ years',
            'focus': 'Business and Financial Data',
            'passion': 'Transforming data into insights'
        },
        'skills': {
            'programming': ['Python', 'HTML/CSS', 'Docker', 'Git', 'SQL'],
            'tools': ['Power BI', 'Excel', 'Tableau'],
            'specialties': ['ETL pipelines', 'Web scraping (BeautifulSoup, Selenium)', 'AWS', 'APIs', 'Business Intelligence', 'Automation', 'Data visualization', 'Exploratory Data Analysis'],
            'frameworks': ['Pandas', 'NumPy', 'Flask', 'Matplotlib']
        },
        'projects': [
            {
                'title': 'Stock Sentiment Analysis',
                'icon': '📊',
                'description': 'A comprehensive NLP pipeline that analyzes market news sentiment to predict stock price movements. Built using Python with Natural Language Processing techniques, this system processes financial news articles and generates sentiment scores to assist in trading decisions.',
                'link': None,
                'link_type': None
            },
            {
                'title': 'Zcreation',
                'icon': '🛍️',
                'description': 'A complete e-commerce product showcase website with custom analytics dashboard. Features include product catalog management, user engagement tracking, and real-time analytics for business insights. Built with modern web technologies and responsive design.',
                'link': 'https://github.com/abdullahsayedparvez/zcreation',
                'link_type': 'repo'
            },
            {
                'title': 'Mehram',
                'icon': '📱',
                'description': 'Backend development for a comprehensive mobile and web application. Currently under development with focus on scalable architecture, API design, and database optimization. Features include user authentication, data management, and real-time functionality.',
                'link': None,
                'link_type': 'private'
            },
            {
                'title': 'Ansaar.in',
                'icon': '🔄',
                'description': 'A full-scale ETL system with interactive dashboards for data visualization and business intelligence. The platform processes large datasets, provides real-time analytics, and offers comprehensive reporting tools for data-driven decision making.',
                'link': 'https://www.ansaar.in/',
                'link_type': 'website'
            },
            {
                'title': 'Resume Builder',
                'icon': '📄',
                'description': 'An automated resume generation web application that allows users to create professional resumes with customizable templates. Features include real-time preview, multiple format exports, and a user-friendly interface for easy resume creation.',
                'link': 'https://resume.glitchdrift.com/',
                'link_type': 'website'
            }
        ],
        'contact': {
            'email': 'abdullahsyed940@gmail.com',
            'linkedin': 'https://www.linkedin.com/in/abdullah-sayed-048149214/',
            'github': 'https://github.com/abdullahsayedparvez',
            'facebook': 'https://www.facebook.com/abdullah.syed.parvez',
            'medium': 'https://medium.com/@abdullahsyed940'
        }
    }
    
    return render_template('index.html', data=portfolio_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
