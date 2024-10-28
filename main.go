package main

import (
	"github.com/nicklasfrahm/solidgo/pkg/solidgo"
)

func main() {
	// Create a simple model
	cube := solidgo.Cube(solidgo.NewVec3(10, 10, 10), false)
	sphere := solidgo.Sphere(5)

	// Translate the sphere
	translatedSphere := solidgo.Translate(solidgo.NewVec3(0, 0, 10), sphere)

	// Combine them with difference
	model := solidgo.Difference(cube, translatedSphere)

	// Save to file
	solidgo.Save(model, "output.scad")
}
