# https://pypi.org/project/wos/#description
#
# from wos import WosClient
# import wos.utils as ut
# # import wos
# q="DOI='10.7546/CRABS.2021.05.03'"
# with WosClient('simeonova@fmi.uni-sofia.bg','practice1@') as client:
#     print(ut.query(client, q))

# import woslite_client as wos

from __future__ import print_function
import time
import woslite_client
from woslite_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: key
apk='clarivate:436bd2ac-728e-471f-b73d-4a3b21ee024f'
configuration = woslite_client.Configuration()
configuration.api_key['X-ApiKey'] = apk

doi='10.7546/CRABS.2021.05.03'



# create an instance of the API class
# create an instance of the API class
api_instance = woslite_client.SearchApi(woslite_client.ApiClient(configuration))
database_id = 'WOS' # str | Database to search. Must be a valid database ID, one of the following: BCI/BIOABS/BIOSIS/CCC/DCI/DIIDW/MEDLINE/WOK/WOS/ZOOREC. WOK represents all databases.
usr_query = 'DOI=(%s)' %(doi) # str | User query for requesting data, ex: TS=(cadmium). The query parser will return errors for invalid queries.
count = 1 # int | Number of records to return, must be 0-100.
first_record = 1 # int | Specific record, if any within the result set to return. Cannot be less than 1 and greater than 100000.
# lang = 'lang_example' # str | Language of search. This element can take only one value: en for English. If no language is specified, English is passed by default. (optional)
# edition = 'edition_example' # str | Edition(s) to be searched. If null, user permissions will be substituted. Must include the name of the collection and edition name separated by '+', ex: WOS+SCI. Multiple editions are separated by ','. Editions available for collection(WOS) - AHCI,CCR,IC,ISSHP,ISTP,SCI,SSCI,BHCI,BSCI and ESCI. (optional)
# publish_time_span = 'publish_time_span_example' # str | This element specifies a range of publication dates. If publishTimeSpan is used, the loadTimeSpan parameter must be omitted. If publishTimeSpan and loadTimeSpan are both omitted, then the maximum time span will be inferred from the editions data. Beginning and end dates should be specified in the yyyy-mm-dd format separated by +, ex: 1993-01-01+2009-12-31. (optional)
# load_time_span = 'load_time_span_example' # str | Load time span (otherwise described as symbolic time span) defines a range of load dates. The load date is the date a record was added to the database. If load date is specified, the publishTimeSpan parameter must be omitted. If both publishTimeSpan and loadTimeSpan are omitted, the maximum publication date will be inferred from the editions data. Any of D/W/M/Y prefixed with a number where D-Day, M-Month, W-Week, Y-Year allowed. Acceptable value range for Day(0-6), Week(1-52), Month(1-12) and Year(0-10), ex: 5D,30W,10M,8Y. (optional)
# sort_field = 'sort_field_example' # str | Order by field(s). Field name and order by clause separated by '+', use A for ASC and D for DESC, ex: PY+D. Multiple values are separated by comma. (optional)

try:
    # Submits a user query and returns results
    # api_response = api_instance.root_get(database_id, usr_query, count, first_record, lang=lang, edition=edition, publish_time_span=publish_time_span, load_time_span=load_time_span, sort_field=sort_field)
    api_response = api_instance.root_get(database_id, usr_query,count, first_record)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->root_get: %s\n" % e)