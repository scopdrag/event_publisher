# Event Publisher #

Python event publisher.
Event driven programming approach.

One can attach multiple event handler and trigger them based on requirements


### What is this repository for? ###

* Officially supports Python 2.6–2.7 & 3.3–3.7

### Usages
```python
from event_publisher import publisher

pub = publisher.Publisher()
def event_handler(event_name, data, earg):
     print(event_name)
     print(data)
 
pub.events += event_handler
data= {'line':"Testing line 1"}
pub.trigger("testing_event", data)

```