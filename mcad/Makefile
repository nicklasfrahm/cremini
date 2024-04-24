PYTHON		:= venv/bin/python3
# Can be overwritten during development to improve preview rendering performance.
RESOLUTION	?= 8

# Configure virtual environment.
$(PYTHON):
	dpkg-query -W python3-venv
	dpkg-query -W python3-pip
	python3 -m venv --prompt mcad venv
	$@ -m pip install --upgrade -r requirements.txt

# Transpile Python code to OpenSCAD program.
build/scad/%.scad: $(PYTHON) src/%.py
	@mkdir -p $(@D)
	./$^

# Generate STL file.
build/stl/%.stl: build/scad/%.scad
	@mkdir -p $(@D)
	@echo "building with resolution: $(RESOLUTION) steps/revolution"
	openscad -o $@ -D 'quality="production"' $^

# Generate PNG file.
build/png/%.png: build/scad/%.scad
	@mkdir -p $(@D)
	openscad -o $@ --imgsize 2048,2048 $^
