let lattitude = 13245
let longitude = 1234

// create post request
let url = URL(string: "https://us-central1-coronapp-b595c.cloudfunctions.net/putPointFeatureEndpoint")!
var request = URLRequest(url: url)
request.httpMethod = "POST"

// insert json data to the request
request.httpBody = "{
  \"type\": \"Feature\",
  \"geometry\": {
    \"type\": \"Point\",
    \"coordinates\": [
      "+lattitude+",
      "+longitude+"
    ]
  }
}"

let task = URLSession.shared.dataTask(with: request) { data, response, error in
    guard let data = data, error == nil else {
        print(error?.localizedDescription ?? "No data")
        return
    }
    print(response)
}