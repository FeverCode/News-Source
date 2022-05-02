import urllib.request,json
from webbrowser import get
from .models import Sources,Articles


#get the api key
api_key  = None

#get news base url
base_url = None

#get articles base url
articles_url = None

def configure_request(app):
    global api_key,base_url,articles_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_BASE_SOURCES_URL']
    articles_url = app.config['ARTICLES_BASE_SOURCES_URL']


def get_sources(category):
    '''
    Function that gets the json response to url request
    '''
    get_sources_url = base_url.format(category,api_key)
    
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        
        
        sources_results = None
        
        
        
        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources(sources_results_list)
    return sources_results

def process_sources(sources_list):
    '''
	Function that processes the news sources results and turns them into a list of objects
	Args:
		sources_list: A list of dictionaries that contain sources details
	Returns:
		sources_results: A list of sources objects
	'''
    sources_results = []
    
    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')
        
        if category:
            sources_object = Sources(id, name, description, url, category, country, language)
            sources_results.append(sources_object)
        
    return sources_results

def get_artcles(id):
    '''
	Function that processes the articles and returns a list of articles objects
	'''
    get_artcles_url = articles_url.format(id,api_key)
    
    with urllib.request.urlopen(get_artcles_url) as url:
        articles_results = json.loads(url.read())
        
        articles_object = None
        if articles_results['articles']:
            articles_object = process_articles(articles_results['articles'])
    
    return articles_object

def process_articles(articles_list):
    """
    _summary_
    
    Args:
        articles_list (_type_): _description_
    """  
    
    articles_object = []
    for article_item in articles_list:
        id = article_item.get('id')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        image = article_item.get('urlToImage')
        date = article_item.get('publishedAt')
        
        if image:
            articles_result = Articles(id,author,title,description,url,image,date)
            articles_object.append(articles_result)
         
    return articles_object
            
      
    
