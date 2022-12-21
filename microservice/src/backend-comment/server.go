package main

import(
	//"fmt"
	"github.com/gin-gonic/gin"
)

func main(){
	r:= gin.Default()

	r.GET("/post", func(c *gin.Context){
		c.JSON(200, gin.H{ // c.JSON serializes Struct into JSON // H is short for map
			"img":"image displayed",
		})
	})

	r.Run() // listen & serve on localhost
}