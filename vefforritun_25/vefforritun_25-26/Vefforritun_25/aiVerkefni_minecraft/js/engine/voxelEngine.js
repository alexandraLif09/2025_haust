// A compact voxel world powered by three.js. Chunked, seeded terrain, fast greedy mesher.
index +=4
}


for(let x=0;x<size;x++) for(let z=0;z<size;z++) for(let y=0;y<h;y++){
const id = at(x,y,z)
if(id===0) continue
// check neighbors to decide which faces to create (6 faces)
// -X
if(!inBounds(x-1,y,z) || at(x-1,y,z)===0) pushFace(x,y,z,-1,0,0,id)
// +X
if(!inBounds(x+1,y,z) || at(x+1,y,z)===0) pushFace(x+1,y,z,1,0,0,id)
// -Z
if(!inBounds(x,y,z-1) || at(x,y,z-1)===0) pushFace(x,y,z-1,0,0,-1,id)
// +Z
if(!inBounds(x,y,z+1) || at(x,y,z+1)===0) pushFace(x,y+0,z+1,0,0,1,id)
// -Y
if(!inBounds(x,y-1,z) || at(x,y-1,z)===0) pushFace(x,y,z,0,-1,0,id)
// +Y
if(!inBounds(x,y+1,z) || at(x,y+1,z)===0) pushFace(x,y+1,z,0,1,0,id)
}


const posArr = new Float32Array(positions)
geom.setAttribute('position', new THREE.BufferAttribute(posArr, 3))
geom.setAttribute('normal', new THREE.BufferAttribute(new Float32Array(normals), 3))
geom.setIndex(indices)
geom.computeBoundingSphere()


// material: one material per chunk using MeshStandardMaterial with vertex colors disabled.
const mat = new THREE.MeshStandardMaterial({vertexColors:false, flatShading:true, wireframe:this.wireframe})
const mesh = new THREE.Mesh(geom, mat)
mesh.castShadow = true
mesh.receiveShadow = true
mesh.position.set(0,0,0)
return mesh
}


toggleWireframe(){
this.wireframe = !this.wireframe
for(const v of this.chunks.values()) v.mesh.material.wireframe = this.wireframe
}


resetWorld(){
// remove all chunk meshes
for(const v of this.chunks.values()) this.scene.remove(v.mesh)
this.chunks.clear()
const r=1
for(let cx=-r;cx<=r;cx++) for(let cz=-r;cz<=r;cz++) this.ensureChunk(cx,cz)
}


setHeldBlock(id){ this.heldBlock = Number(id) }
}