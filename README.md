# Shipments

This is a simple demo project based on VueJS and Django.

> This GitHub repo contains backend part. Frontend can be found by this [link](https://github.com/soulless-viewer/shipments).

## Installation

Install the packages with pip:

```bash
$ pip install -r requirements.txt
```

## Usage

Run dev server with the following command:

```bash
$ python manage.py runserver 0.0.0.0:8000
```

Now you can access your API at [127.0.0.1:8000](http://127.0.0.1:8000/api/v1/shipment/)

### API Doc

*[GET] Get shipments*
~~~
/api/v1/shipment/?page=3&page_size=1

200

<<<
{
    "page": 3,
    "count": 29,
    "next": "http://127.0.0.1:8000/api/v1/shipment/?page=4&page_size=1",
    "previous": "http://127.0.0.1:8000/api/v1/shipment/?page=2&page_size=1",
    "page_size": 6,
    "results": [
        {
            "id": 36,
            "arrival_dt": "2022-05-10T05:53:00Z",
            "departure_dt": "2022-05-12T05:53:00Z",
            "cargo_volume": 100,
            "arrival_point": "London",
            "departure_point": "Minsk"
        }
    ]
}
~~~

*[POST] Create shipment*
~~~
/api/v1/shipment/

200

>>>
{    
    "arrival_dt": "2022-05-10T05:53:00Z",
    "departure_dt": "2022-05-12T05:53:00Z",
    "cargo_volume": 100,
    "arrival_point": "London",
    "departure_point": "Minsk"
}

<<<
{    
    "id": 36,
    "arrival_dt": "2022-05-10T05:53:00Z",
    "departure_dt": "2022-05-12T05:53:00Z",
    "cargo_volume": 100,
    "arrival_point": "London",
    "departure_point": "Minsk"
}
~~~

*[GET] Get shipment by ID*
~~~
/api/v1/shipment/1/

200

<<<
{    
    "id": 1,
    "arrival_dt": "2022-05-10T05:53:00Z",
    "departure_dt": "2022-05-12T05:53:00Z",
    "cargo_volume": 100,
    "arrival_point": "London",
    "departure_point": "Minsk"
}
~~~

*[PUT] Update shipment by ID*
~~~
/api/v1/shipment/1/

200

>>>
{    
    "arrival_dt": "2022-05-10T05:53:00Z",
    "departure_dt": "2022-05-12T05:53:00Z",
    "cargo_volume": 100,
    "arrival_point": "London",
    "departure_point": "Minsk"
}

<<<
{    
    "id": 1,
    "arrival_dt": "2022-05-10T05:53:00Z",
    "departure_dt": "2022-05-12T05:53:00Z",
    "cargo_volume": 100,
    "arrival_point": "London",
    "departure_point": "Minsk"
}
~~~

*[DELETE] Remove shipment by ID*
~~~
/api/v1/shipment/1/

204
~~~

> Swagger will be added later

## Testing

Nothing really special, but anyway I will show)

```bash
$ python manage.py test
```

## Contributing

1.  Fork it.
2.  Create your feature branch:  `git checkout -b my-new-feature`
3.  Commit your changes:  `git commit -am 'Add some feature'`
4.  Push to the branch:  `git push origin my-new-feature`
5.  Submit a pull request

## License
The MIT License (MIT)

Copyright (c) 2022 Mikalai Lisitsa

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
