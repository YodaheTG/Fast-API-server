import requests

response = requests.post('https://services.sentinel-hub.com/api/v1/process',
  headers={"Authorization" : "Bearer eyJraWQiOiJzaCIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI0ZTExMGMzMS04NDVlLTQ2ZjYtODVmNS02ODEwMDNlZmVlMzEiLCJhdWQiOiIxOWUwN2EzZS1kZDU1LTQxNDctYmE5YS1kZDczM2E0NjhlZWUiLCJqdGkiOiI4YTFkNGE1Yy1mNmJkLTRmN2EtYWYxNi0xMWVjMWQyZGRjYTEiLCJleHAiOjE2Njc3Mjg5ODEsIm5hbWUiOiJZb3VkYWhlIEdlYnJlbWFyaWFtIiwiZW1haWwiOiJ5b2RnaXNAZ21haWwuY29tIiwiZ2l2ZW5fbmFtZSI6IllvdWRhaGUiLCJmYW1pbHlfbmFtZSI6IkdlYnJlbWFyaWFtIiwic2lkIjoiMjhmZTY2ZjctNGY0Ny00MTMxLWIwNGUtZjAzYmQxMmE2MmVhIiwiZGlkIjoxLCJhaWQiOiIxOWY3OTI4Zi0zZTM4LTRlYTAtYThkYy1jMDhjNzYyYWY0NzYiLCJkIjp7IjEiOnsicmEiOnsicmFnIjoxfSwidCI6MTEwMDB9fX0.nUz5B9VQkRDUNrnCeaG-IkPWR6cVz-J9UgwNEC84V3ZXH4fQZMOytNwgagYfI04OkH-GXiOEb03HPIy50AoMYznO5SJtaqosjhNQU_j7wOO6UaYDuCdkPrslY8jl-coDfxd4GZTs28ukAaW3X2ocbA0rJSpFkK_bks9Omu8gXcT6xNl62cvw6UJbcv-D4UxFBt3jE9eGIE2GYdefmg42rCVto7cjeU8mpTYLb2Iy2jf-h8GYNd4gTJ9OzfjdSE8M8yadaSLf9yfZv41ABFPydIUa4XvyZVArW3ujDNV48TdYDqla_OxDXPwerorP1UBvSTKhZsqZDzSMSZxlWwvgdg"
  ,"Accept":"image/png"},
  
  json={
    "input": {
        "bounds": {
            "bbox": [
                13.822174072265625,
                45.85080395917834,
                14.55963134765625,
                46.29191774991382
            ]
        },
        "data": [{
            "type": "sentinel-2-l2a"
        }]
    },
     "output":{
        "width":100,
        "height": 100

    },
   
    "evalscript": """
    //VERSION=3

    function setup() {
      return {
        input: ["B02", "B03", "B04"],
        output: {
          bands: 3
        }
      };
    }

    function evaluatePixel(
      sample,
      scenes,
      inputMetadata,
      customData,
      outputMetadata
    ) {
      return [2.5 * sample.B04, 2.5 * sample.B03, 2.5 * sample.B02];
    }
    """
})
print (response)

with open('test2.png', 'wb') as f:
    f.write(response.content)