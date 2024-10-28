package solidgo

import (
	"fmt"
	"os"
	"strings"
)

// Vec3 represents a 3D vector.
type Vec3 struct {
	X, Y, Z float64
}

// NewVec3 creates a new Vec3.
func NewVec3(x, y, z float64) Vec3 {
	return Vec3{X: x, Y: y, Z: z}
}

// Node represents a generic OpenSCAD object
type Node interface {
	String() string
}

// PrimitiveNode represents basic shapes
type PrimitiveNode struct {
	name     string
	params   map[string]interface{}
	children []Node
}

// TransformNode represents transformations
type TransformNode struct {
	name     string
	params   map[string]interface{}
	children []Node
}

// Cube creates a cube primitive
func Cube(size Vec3, center bool) Node {
	return &PrimitiveNode{
		name: "cube",
		params: map[string]interface{}{
			"size":   size,
			"center": center,
		},
	}
}

// Sphere creates a sphere primitive
func Sphere(radius float64) Node {
	return &PrimitiveNode{
		name: "sphere",
		params: map[string]interface{}{
			"r": radius,
		},
	}
}

// Cylinder creates a cylinder primitive
func Cylinder(height, radius float64, center bool) Node {
	return &PrimitiveNode{
		name: "cylinder",
		params: map[string]interface{}{
			"h":      height,
			"r":      radius,
			"center": center,
		},
	}
}

// Translate creates a translation transformation
func Translate(v Vec3, child Node) Node {
	return &TransformNode{
		name: "translate",
		params: map[string]interface{}{
			"v": v,
		},
		children: []Node{child},
	}
}

// Rotate creates a rotation transformation
func Rotate(v Vec3, child Node) Node {
	return &TransformNode{
		name: "rotate",
		params: map[string]interface{}{
			"a": v,
		},
		children: []Node{child},
	}
}

// Scale creates a scaling transformation
func Scale(v Vec3, child Node) Node {
	return &TransformNode{
		name: "scale",
		params: map[string]interface{}{
			"v": v,
		},
		children: []Node{child},
	}
}

// Union combines multiple shapes with union operation
func Union(children ...Node) Node {
	return &TransformNode{
		name:     "union",
		children: children,
	}
}

// Difference subtracts subsequent shapes from the first shape
func Difference(children ...Node) Node {
	return &TransformNode{
		name:     "difference",
		children: children,
	}
}

// Intersection creates intersection of shapes
func Intersection(children ...Node) Node {
	return &TransformNode{
		name:     "intersection",
		children: children,
	}
}

// String methods for Vec3
func (v Vec3) String() string {
	return fmt.Sprintf("[%g, %g, %g]", v.X, v.Y, v.Z)
}

// String methods for PrimitiveNode
func (n *PrimitiveNode) String() string {
	params := make([]string, 0, len(n.params))
	for k, v := range n.params {
		params = append(params, fmt.Sprintf("%s=%v", k, v))
	}
	return fmt.Sprintf("%s(%s);", n.name, strings.Join(params, ", "))
}

// String methods for TransformNode
func (n *TransformNode) String() string {
	var params string
	if len(n.params) > 0 {
		paramsList := make([]string, 0, len(n.params))
		for k, v := range n.params {
			paramsList = append(paramsList, fmt.Sprintf("%s=%v", k, v))
		}
		params = strings.Join(paramsList, ", ")
	}

	var result strings.Builder
	result.WriteString(n.name)
	result.WriteString("(")
	if params != "" {
		result.WriteString(params)
	}
	result.WriteString(")")
	result.WriteString(" {\n")

	for _, child := range n.children {
		childStr := child.String()
		// Indent child lines
		lines := strings.Split(childStr, "\n")
		for _, line := range lines {
			result.WriteString("  ")
			result.WriteString(line)
			result.WriteString("\n")
		}
	}

	result.WriteString("}")
	return result.String()
}

// Save writes the OpenSCAD code to a file
func Save(node Node, filename string) error {
	scadCode := node.String()

	file, err := os.OpenFile(filename, os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		return fmt.Errorf("failed to open file: %w", err)
	}

	_, err = file.WriteString(scadCode)
	if err != nil {
		return fmt.Errorf("failed to write to file: %w", err)
	}

	return nil
}
