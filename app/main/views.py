from flask import render_template
from . import main
from ..requests import get_sources,get_artcles
from ..models import Sources

@main.route('/')
def index():
    '''
    view root page function that returns the index the page and its data
    '''
    sources = get_sources('business')
    sport_sources = get_sources('sports')
    technology_sources = get_sources('technology')
    entertainment_sources = get_sources('entertainment')
    title = "News Source"
    
    return render_template('index.html',title=title, sources = sources, sport_sources = sport_sources, technology_sources = technology_sources,entertainment_sources = entertainment_sources)

@main.route('/sources/<int:id>')
def articles(id):
    '''
    View articles pages
    '''
    articles = get_artcles(id)
    title= f'NS | {id}'
    
    return render_template('articles.html',title=title,articles=articles)