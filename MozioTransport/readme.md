# mozio-transport

Welcome to MozioTransport API. You can use this API to access all API endpoints, 
such as Provider API to look up transportation suppliers and Area API to look up 
services areas coverage related to a provider. <br> <br>
The API is organized around REST and all resquests and responses are encoded in JSON. <br> 
API is available at `https://mozio-transport.herokuapp.com/` <br>

Let's start deals with methods descriptions. <br>

**Provider**
----

**Get list of provider**
  Returns json data about list of all provider.

* **Sample Call:**
  `curl https://mozio-transport.herokuapp.com/providers`

* **URL**
  /providers/

* **Method:**
  `GET`
  
*  **URL Params**
  None   

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `
[
    {
        "name": "Mozio1",
        "email": "admin@gmail.com",
        "phone_number": "+123456789",
        "language": "fr",
        "currency": "1536.00"
    },
    {
        "name": "Mozio2",
        "email": "admin2@gmail.com",
        "phone_number": "+3345698769",
        "language": "en",
        "currency": "2000.00"
    }
]`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ detail : "Not found." }`

<br>

**Get a single provider**
  Returns json data about a single provider.

* **Sample Call:**
  `curl https://mozio-transport.herokuapp.com/providers/id`

* **URL**
  /providers/:id

* **Method:**
  `GET`
  
*  **URL Params**
  `id=[integer]` 

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `
{
    "name": "Mozio1",
    "email": "admin@gmail.com",
    "phone_number": "+123456789",
    "language": "fr",
    "currency": "1536.00"
}`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ detail : "Not found." }`


<br>

**Create a provider**
  Returns 201 HTTP response.

* **Sample Call:**
  `curl https://mozio-transport.herokuapp.com/providers/`

* **URL**
  /providers/

* **Method:**
  `POST`
  
*  **URL Params**
  None

* **Data Params**
  `
  {
      "name": "Mozio1",
      "email": "admin@gmail.com",
      "phone_number": "+123456789",
      "language": "fr",
      "currency": "1536.00"
  }`

* **Success Response:**

  * **Code:** 201 <br />
    **Content:** None
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ detail : "Not found." }`


<br>

**Update a provider**
  Returns updated json data about a single provider.

* **Sample Call:**
  `curl https://mozio-transport.herokuapp.com/providers/id`

* **URL**
  /providers/:id

* **Method:**
  `PUT`
  
*  **URL Params**
  `id=[integer]` 

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `
{
    "name": "Mozio1",
    "email": "admin@gmail.com",
    "phone_number": "+123456789",
    "language": "fr",
    "currency": "1536.00"
}`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ detail : "Not found." }`


<br>

**Delete a provider**
  Returns 204 HTTP response.

* **Sample Call:**
  `curl https://mozio-transport.herokuapp.com/providers/id`

* **URL**
  /providers/:id

* **Method:**
  `DELETE`
  
*  **URL Params**
  `id=[integer]` 

* **Success Response:**

  * **Code:** 204 <br />
    **Content:** None
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ detail : "Not found." }`


<br> <br> 

**Area**
----

**Get list of ares**
  Returns json data about list of all areas.

* **Sample Call:**
  `curl https://mozio-transport.herokuapp.com/areas`

* **URL**
  /areas/

* **Method:**
  `GET`
  
*  **URL Params**
  None   

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `
[
    {
        "name": "AreaTown1",
        "price": 5000,
        "provider": "Mozio11",
        "poly": "SRID=4326;POLYGON ((2.312622 6.440859, 2.422485 6.473609, 2.504883 6.397189, 2.312622 6.440859))"
    },
    {
        "name": "AreaTown2",
        "price": 16000,
        "provider": "Mozio2",
        "poly": "SRID=4326;POLYGON ((-3.22998 53.080827, -0.878906 52.882391, -0.812988 52.241256, -2.526855 51.835778, -3.88916 52.415823, -3.22998 53.080827))"
    },
    {
        "name": "AreaTown3",
        "price": 7500,
        "provider": "Mozio11",
        "poly": "SRID=4326;POLYGON ((-105.380859 37.822802, -105.292969 34.741612, -100.458984 34.633208, -100.151367 37.26531, -98.74511699999999 39.095963, -100.678711 39.53794, -105.380859 37.822802))"
    }
]`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ detail : "Not found." }`

<br>

**Get a single area**
  Returns json data about a single area.

* **Sample Call:**
  `curl https://mozio-transport.herokuapp.com/areas/id`

* **URL**
  /areas/:id

* **Method:**
  `GET`
  
*  **URL Params**
  `id=[integer]` 

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `
{
        "name": "AreaTown2",
        "price": 16000,
        "provider": "Mozio2",
        "poly": "SRID=4326;POLYGON ((-3.22998 53.080827, -0.878906 52.882391, -0.812988 52.241256, -2.526855 51.835778, -3.88916 52.415823, -3.22998 53.080827))"
    }`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ detail : "Not found." }`


<br>

**Create an area**
  Returns 201 HTTP response.

* **Sample Call:**
  `curl https://mozio-transport.herokuapp.com/areas/`

* **URL**
  /areas/

* **Method:**
  `POST`
  
*  **URL Params**
  None

* **Data Params**
  `{
        "name": "AreaTown2",
        "price": 16000,
        "provider": "Mozio2",
        "poly": "SRID=4326;POLYGON ((-3.22998 53.080827, -0.878906 52.882391, -0.812988 52.241256, -2.526855 51.835778, -3.88916 52.415823, -3.22998 53.080827))"
    }`

* **Success Response:**

  * **Code:** 201 <br />
    **Content:** None
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ detail : "Not found." }`


<br>

**Update an**
  Returns updated json data about a single area.

* **Sample Call:**
  `curl https://mozio-transport.herokuapp.com/areas/id`

* **URL**
  /areas/:id

* **Method:**
  `PUT`
  
*  **URL Params**
  `id=[integer]` 

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `
{
    "name": "AreaTown1",
    "price": 5000,
    "provider": "Mozio11",
    "poly": "SRID=4326;POLYGON ((2.312622 6.440859, 2.422485 6.473609, 2.504883 6.397189, 2.312622 6.440859))"
}`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ detail : "Not found." }`


<br>

**Delete an area**
  Returns 204 HTTP response.

* **Sample Call:**
  `curl https://mozio-transport.herokuapp.com/areas/id`

* **URL**
  /areas/:id

* **Method:**
  `DELETE`
  
*  **URL Params**
  `id=[integer]` 

* **Success Response:**

  * **Code:** 204 <br />
    **Content:** None
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ detail : "Not found." }`


<br>

**Get list of polygons which contains point defined by lat and lng coordinates**
  Returns json data about list of areas which its polygons contains 
  a point specified by latitude and longitude parameters in URL.

* **Sample Call:**
  `curl https://mozio-transport.herokuapp.com/areas/lati/lngi`

* **URL**
  /areas/:lati/:lngi

* **Method:**
  `GET`
  
*  **URL Params**
  `lati=[float] and lngi=[float]` 

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `
{
        "name": "AreaTown2",
        "price": 16000,
        "provider": "Mozio2",
        "poly": "SRID=4326;POLYGON ((-3.22998 53.080827, -0.878906 52.882391, -0.812988 52.241256, -2.526855 51.835778, -3.88916 52.415823, -3.22998 53.080827))"
    }`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ detail : "Not found." }`