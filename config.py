import os
#from app.utils.model import Model
import json

import enchant.checker as spellcheck
chkr = spellcheck.SpellChecker("en_GB")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.join(BASE_DIR, 'app')

PATH_UDPIPE_MODEL = os.path.join(BASE_DIR, 'data', 'models', 'english-partut-ud-2.3-181115.udpipe')
#UDPIPE_MODEL = Model(PATH_UDPIPE_MODEL)

PATH_LISTS = os.path.join(BASE_DIR, 'data', 'lists', 'lists.json')
with open(PATH_LISTS, encoding='utf-8') as data_file:
    lists = json.load(data_file)
FIVE_T_FREQ_COCA = lists['5000frequentCOCA']
FREQ_VERBS_COCA_FROM_FIVE_T = lists['frequentverbsCOCAfrom5000']
UWL = lists['UWL']

OPEN_CLASS = ['NOUN', 'VERB', 'ADV', 'ADJ', 'PROPN']

PATH_LINKINGS = os.path.join(BASE_DIR, 'data', 'lists', 'linkings.json')
with open(PATH_LINKINGS, encoding='utf-8') as data_file:
    LINKINGS = json.load(data_file)

PATH_FUNC_NGRAMS = os.path.join(BASE_DIR, 'data', 'lists', 'functional_ngrams.json')
with open(PATH_FUNC_NGRAMS, encoding='utf-8') as data_file:
    FUNC_NGRAMS = json.load(data_file)

PATH_SUFFIXES = os.path.join(BASE_DIR, 'data', 'lists', 'suffixes.json')
with open(PATH_SUFFIXES, encoding='utf-8') as data_file:
    SUFFIXES = json.load(data_file)

PATH_NGRAMS = os.path.join(BASE_DIR, 'data', 'lists', 'ngrams.txt')
with open(PATH_NGRAMS, encoding='utf-8') as data_file:
    NGRAMS = [x.split() for x in data_file.read().split('\n')]

PATH_CONNECTORS = os.path.join(BASE_DIR, 'data', 'lists', 'connectors.txt')
with open(PATH_CONNECTORS, 'r', encoding='utf-8') as data_file:
    CONNECTORS = data_file.read().strip()

DONS = [
    'thing', 'fact', 'point', 'argument', 'result', 'dispute',
    'problem', 'factor', 'approach', 'view', 'feeling', 'process',
    'theme', 'attempt', 'controversy', 'statement', 'task', 'issue',
    'dream', 'matter', 'situation', 'need', 'reason', 'solution',
    'possibility', 'change', 'debate', 'sense', 'method', 'theory',
    'finding', 'question', 'idea', 'concept', 'opinion', 'ideas', 'things'
]

NUM_LIST = ['millions', 'hundreds',
            'thousands', 'milliards',
            'billions', 'trillions']

numeric_features = ['av_depth', 'max_depth', 'min_depth', 'num_acl', 'num_rel_cl', 'num_advcl', 'num_sent', 'num_tok',
                    'av_tok_before_root', 'av_len_sent', 'num_cl', 'num_tu', 'num_compl_tu', 'num_coord', 'num_poss',
                    'num_prep', 'num_adj_noun', 'num_part_noun', 'num_noun_inf', 'pos_sim_nei', 'pos_sim_all',
                    'lemma_sim_all', 'lemma_sim_nei', 'density', 'ls', 'corrected_vs', 'lfp_1000', 'lfp_2000',
                    'lfp_uwl', 'lfp_rest', 'ndw', 'corrected_ttr', 'lv', 'corrected_vv', 'vvii', 'nv', 'adjv', 'advv',
                    'modv', 'der_level3', 'der_level4', 'der_level5', 'der_level6', 'mci', 'freq_finite_forms',
                    'freq_aux', 'num_inf', 'num_gerunds', 'num_pres_sing', 'num_pres_plur', 'num_past_part',
                    'num_past_simple', 'num_linkings', 'num_4grams', 'num_func_ngrams', 'num_shell_noun',
                    'num_misspelled_tokens', 'million_mistake', 'sum_punct'
                    ]

important_features = ['av_depth', 'max_depth', 'min_depth', 'num_acl', 'num_rel_cl', 'num_advcl', 'num_sent', 'num_tok',
                      'av_tok_before_root', 'av_len_sent', 'num_cl', 'num_tu', 'num_compl_tu', 'num_coord', 'num_poss',
                      'num_prep', 'num_adj_noun', 'num_part_noun', 'num_noun_inf', 'pos_sim_nei', 'pos_sim_all',
                      'lemma_sim_all', 'lemma_sim_nei', 'density', 'ls', 'corrected_vs', 'lfp_1000', 'lfp_2000',
                      'lfp_uwl', 'lfp_rest', 'ndw', 'corrected_ttr', 'lv', 'corrected_vv', 'vvii', 'nv', 'adjv', 'advv',
                      'modv', 'der_level3', 'der_level4', 'der_level5', 'der_level6', 'mci', 'freq_finite_forms',
                      'freq_aux', 'num_inf', 'num_gerunds', 'num_pres_sing', 'num_pres_plur', 'num_past_part',
                      'num_past_simple', 'num_linkings', 'num_4grams', 'num_func_ngrams', 'million_mistake', 'sum_punct']

feature_mapping = {
    'corrected_vv': 'Verb variation',
    'num_linkings': 'Number of linking phrases',
    'av_len_sent': 'Average length of the sentence',
    'ls': 'Lexical sophistication',
    'num_gerunds': 'Number of gerunds',
    'nv': 'Noun variation',
    'num_inf': 'Number of infinitives',
    'ndw': 'Number of lemmas',
    'num_func_ngrams': 'Number of functional n-grams',
    'num_cl': 'Number of clauses',
    'num_acl': 'Number of adjectival clauses',
    'av_tok_before_root': 'Average number of words before root',
    'num_sent': 'Number of sentences',
    'num_past_simple': 'Number of verbs in past simple',
    'freq_aux': 'Number of auxilaries',
    'corrected_vs': 'Verb sophistication',
    'density': 'Lexical density',
    'num_coord': 'Number of coordinated phrases',
    'num_poss': 'Number of possessives',
    'der_level5': 'Derivational level 5',
    'der_level3': 'Derivational level 3',
    'der_level4': 'Derivational level 4',
    'der_level6': 'Derivational level 6'
}

feature_feedback_to_improve = {
    'corrected_vv': 'different verbs',
    'num_linkings': 'linking phrases',
    'av_len_sent': 'large sentences',
    'ls': 'academic words',
    'num_gerunds': 'gerunds',
    'nv': 'different nouns',
    'num_inf': 'infinitives',
    'ndw': 'different words',
    'num_func_ngrams': 'functional n-grams',
    'num_cl': 'complex sentences',
    'num_acl': 'relative clauses',
    'av_tok_before_root': 'words before the main predicate',
    'num_sent': 'sentences',
    'num_past_simple': 'verbs in past simple',
    'freq_aux': 'auxiliary verbs',
    'corrected_vs': 'sophisticated verbs',
    'density': 'nouns, verbs, adverbs, and adjectives',
    'num_coord': 'coordinate constructions',
    'num_poss': 'possessive constructions',
    'der_level5': 'morphologically complex words',
    'der_level3': 'morphologically complex words',
    'der_level4': 'morphologically complex words',
    'der_level6': 'morphologically complex words'
}

feature_feedback_best = {
    'corrected_vv': 'different verbs',
    'num_linkings': 'linking phrases',
    'av_len_sent': 'long sentences',
    'ls': 'academic words',
    'num_gerunds': 'gerunds',
    'nv': 'different nouns',
    'num_inf': 'infinitives',
    'ndw': 'different words',
    'num_func_ngrams': 'functional n-grams',
    'num_cl': 'complex sentences',
    'num_acl': 'relative clauses',
    'av_tok_before_root': 'words before the main predicate',
    'num_sent': 'sentences',
    'num_past_simple': 'verbs in past simple',
    'freq_aux': 'auxiliary verbs',
    'corrected_vs': 'sophisticated verbs',
    'density': 'nouns, verbs, adverbs, and adjectives',
    'num_coord': 'coordinate constructions',
    'num_poss': 'possessive constructions',
    'der_level5': 'morphologically complex words',
    'der_level3': 'morphologically complex words',
    'der_level4': 'morphologically complex words',
    'der_level6': 'morphologically complex words'
}

feature_hints = {
    'Lexical density': ' is the ratio of the number of lexical words (nouns, adjectives, verbs, and adverbs) to the'
                       ' total number of words in a text.',
    'Number of possessives': ': possessives are forms that we use to talk about possessions and relationships between'
                             ' things and people, for example: <em>mother\'s smile</em>, <em>the clothes of my'
                             ' father</em>.',
    'Number of coordinated phrases': ': only adjectives, adverbs, nouns and verb phrases can be coordinated, for'
                                     ' example: <em>She is <strong>beautiful and smart</strong></em>. <em>He <strong>'
                                     'smiled and went away</strong></em>',
    'Number of auxilaries': ' <em>have</em>, <em>do</em>, <em>be</em>, <em>can</em>, <em>should</em>, <em>must</em>...',
    'Average number of words before root': ': a root is a main verb of the sentence, for example: <em><strong>She'
                                           '</strong> is beautiful and smart</em>. <em><strong>My mother</strong> went'
                                           ' to help them</em>.',
    'Number of adjectival clauses': ': an adjectival clause is a clause that modifies nominal phrase (noun), for'
                                    ' example: <em>There are many online sites <strong>offering booking facilities'
                                    '</strong></em>.',
    'Number of functional n-grams': ': functional n-grams are frequent organising collocations, for example: <em>is'
                                    ' totally different from</em>, <em>a large amount of</em>.',
    'Derivational level 3': ': the number of words with suffixes from <a href="https://www.pdffiller.com/jsfiller-'
                            'desk14/?projectId=301149742&expId=5010&expBranch=3#1f2d9152ddc848798c5e2e06bc4db69c">'
                            '(Bauer and Nation 1993)</a>, for example: -<em>able</em> (<em>readable</em>),'
                            ' -<em>er</em> (<em>reader</em>), -<em>ish</em> (<em>freakish</em>), -<em>less</em>'
                            ' (<em>peerless</em>), -<em>ly</em> (<em>quickly</em>).',
    'Derivational level 4': ': the number of words with suffixes from <a href="https://www.pdffiller.com/jsfiller-'
                            'desk14/?projectId=301149742&expId=5010&expBranch=3#1f2d9152ddc848798c5e2e06bc4db69c">'
                            '(Bauer and Nation 1993)</a>, for example: -<em>tion</em> (<em>attention</em>), -<em>ess'
                            '</em> (<em>happiness</em>), -<em>ful</em> (<em>wonderful</em>), -<em>ism</em> (<em>'
                            'realism</em>), -<em>ist</em> (<em>specialist</em>), -<em>ity</em> (<em>civility</em>).',
    'Derivational level 5': ': the number of words with suffixes from <a href="https://www.pdffiller.com/jsfiller-'
                            'desk14/?projectId=301149742&expId=5010&expBranch=3#1f2d9152ddc848798c5e2e06bc4db69c">'
                            '(Bauer and Nation 1993)</a>, for example: -<em>age</em> (<em>percentage</em>), -<em>al'
                            '</em> (<em>approval</em>), -<em>ally</em> (<em>idiotically</em>), -<em>an</em>'
                            ' (<em>Russian</em>).',
    'Derivational level 6': ': the number of words with suffixes from <a href="https://www.pdffiller.com/jsfiller-'
                            'desk14/?projectId=301149742&expId=5010&expBranch=3#1f2d9152ddc848798c5e2e06bc4db69c">'
                            '(Bauer and Nation 1993)</a>, for example: -<em>ee</em> (<em>attendee</em>), -<em>ic</em>'
                            ' (<em>poetic</em>), -<em>ify</em> (<em>intensify</em>).',
    'Number of sentences': ': a sentence is a group of words that is separated from another such group by a full stop,'
                           ' a question mark, an exclamation mark, a quotation mark, or suspension points.',
    'Number of clauses': ': a clause is a structure with a subject and a predicate, for example: <em>I read a book,'
                         ' Lola danced.</em> - 2 clauses.',
    'Number of lemmas': ' <em>I am fine</em> - 3 lemmas (<em>I</em>, <em>be</em>, <em>fine</em>).',
    'Number of infinitives': ' <em>to read</em>, <em>to dance</em>.',
    'Noun variation': ' is the ratio of the number of nouns to the total number of lexical words (nouns, adjectives,'
                      ' verbs, and adverbs) in a text.',
    'Verb variation': ' is the ratio of the number of verbs to the total number of lexical words (nouns, adjectives,'
                      ' verbs, and adverbs) in a text.',
    'Lexical sophistication': ' is the ratio of the number of advanced words to the total number of words.',
    'Number of linking phrases': ' <em>besides</em>, <em>however</em>, <em>in conclusion</em>...',
    'Average length of the sentence': ': the average number of words per sentence.',
    'Number of gerunds': ' <em>doing</em>, <em>smiling</em>, <em>running</em>...',
    'Number of verbs in past simple': ': <em>smiled</em>, <em>looked</em>, <em>tried</em>...',
    'Verb sophistication': ' is the ratio of the number of advanced verbs to the total number of words.'
}