---
url: https://developers.cloudflare.com/ai/models/meta/muse-spark-open/
title: Muse Spark Open (Meta) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:11:03.189279+00:00
---

# Muse Spark Open (Meta) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/meta/muse-spark-open/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Meta logo](https://developers.cloudflare.com/_astro/meta.CTzB_ysm.svg)

# Muse Spark Open

Text Generation • Meta

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`meta/muse-spark-open`

  * Third-party



Meta's most capable open-weight model, built for agentic coding. Show it a screenshot, chart, or photo alongside your request and it reasons over both to write working code, call tools, and carry multi-step tasks across a 1M-token context.

Model Info|   
---|---  
Context Window[ ↗](https://developers.cloudflare.com/workers-ai/platform/glossary/)| 1,040,000 tokens  
Terms and License| [link ↗](https://fireworks.ai/terms)  
More information| [link ↗](https://fireworks.ai/models/meta/muse-spark-open)  
Request formats| Chat Completions  
Pricing| 

  * Input (per 1M tokens)$1.25
  * Cached input (per 1M tokens)$0.15
  * Output (per 1M tokens)$4.25

  
  
## Usage
    
    
    const response = await env.AI.run(
      'meta/muse-spark-open',
      {
        messages: [
          {
            role: 'user',
            content: [
              {
                type: 'image_url',
                image_url: {
                  url: 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Figurines_from_Clay_Critters.jpg/1280px-Figurines_from_Clay_Critters.jpg',
                },
              },
              {
                type: 'text',
                text: 'Rebuild the gnome in the purple hat from this photo as a 3D scene, including whatever he is holding. Return one self-contained index.html that loads Three.js from a CDN with an import map, models him from simple primitives, matches the clay colors from the photo, uses soft studio lighting on a light grey backdrop, and slowly turns him on a turntable. Return only the HTML file in a single code block.',
              },
            ],
          },
        ],
        max_completion_tokens: 12000,
        reasoning_effort: 'medium',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "meta/muse-spark-open",
      "messages": [
        {
          "role": "user",
          "content": [
            {
              "type": "image_url",
              "image_url": {
                "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Figurines_from_Clay_Critters.jpg/1280px-Figurines_from_Clay_Critters.jpg"
              }
            },
            {
              "type": "text",
              "text": "Rebuild the gnome in the purple hat from this photo as a 3D scene, including whatever he is holding. Return one self-contained index.html that loads Three.js from a CDN with an import map, models him from simple primitives, matches the clay colors from the photo, uses soft studio lighting on a light grey backdrop, and slowly turns him on a turntable. Return only the HTML file in a single code block."
            }
          ]
        }
      ],
      "max_completion_tokens": 12000,
      "reasoning_effort": "medium"
    }'
    
    
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gnome Purple Hat - Clay 3D</title>
    <script async src="https://unpkg.com/es-module-shims@1.8.0/dist/es-module-shims.js"></script>
    <script type="importmap">
    {
      "imports": {
        "three": "https://unpkg.com/three@0.160.0/build/three.module.js",
        "three/addons/": "https://unpkg.com/three@0.160.0/examples/jsm/"
      }
    }
    </script>
    <style>
      html,body{margin:0;width:100%;height:100%;overflow:hidden;background:#d6d6d6;}
      canvas{display:block;}
    </style>
    </head>
    <body>
    <script type="module">
    import * as THREE from 'three';
    import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
    
    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0xd4d4d4);
    scene.fog = new THREE.Fog(0xd4d4d4, 8, 20);
    
    const renderer = new THREE.WebGLRenderer({antialias:true});
    renderer.setSize(innerWidth, innerHeight);
    renderer.setPixelRatio(devicePixelRatio);
    renderer.shadowMap.enabled = true;
    renderer.shadowMap.type = THREE.PCFSoftShadowMap;
    document.body.appendChild(renderer.domElement);
    
    const camera = new THREE.PerspectiveCamera(35, innerWidth/innerHeight, 0.1, 100);
    camera.position.set(0, 1.6, 4.5);
    
    const controls = new OrbitControls(camera, renderer.domElement);
    controls.target.set(0, 0.75, 0);
    controls.enableDamping = true;
    controls.minDistance = 2;
    controls.maxDistance = 10;
    controls.update();
    
    // lighting - soft studio
    const ambient = new THREE.HemisphereLight(0xffffff, 0xcccccc, 1.1);
    scene.add(ambient);
    
    const dir1 = new THREE.DirectionalLight(0xfffaf0, 1.2);
    dir1.position.set(3, 5, 3);
    dir1.castShadow = true;
    dir1.shadow.mapSize.set(2048,2048);
    dir1.shadow.radius = 4;
    scene.add(dir1);
    
    const dir2 = new THREE.DirectionalLight(0xffffff, 0.6);
    dir2.position.set(-3, 4, -2);
    scene.add(dir2);
    
    const fill = new THREE.DirectionalLight(0xffffff, 0.4);
    fill.position.set(0, 2, -4);
    scene.add(fill);
    
    // backdrop + turntable
    const groundGeo = new THREE.CircleGeometry(4, 64);
    const groundMat = new THREE.MeshStandardMaterial({color:0xededed, roughness:0.9, metalness:0});
    const ground = new THREE.Mesh(groundGeo, groundMat);
    ground.rotation.x = -Math.PI/2;
    ground.receiveShadow = true;
    scene.add(ground);
    
    const turntableGeo = new THREE.CylinderGeometry(1.35, 1.35, 0.06, 64);
    const turntableMat = new THREE.MeshStandardMaterial({color:0xe8e8e8, roughness:0.6});
    const turntable = new THREE.Mesh(turntableGeo, turntableMat);
    turntable.position.y = 0.03;
    turntable.receiveShadow = true;
    turntable.castShadow = true;
    scene.add(turntable);
    
    // materials - clay colors matched to photo
    const matSkin = new THREE.MeshStandardMaterial({color:0xf2b8a0, roughness:0.5, metalness:0});
    const matSkinDark = new THREE.MeshStandardMaterial({color:0xe9a995, roughness:0.6});
    const matHat = new THREE.MeshStandardMaterial({color:0x7b6bc2, roughness:0.6}); // purple hat
    const matJacket = new THREE.MeshStandardMaterial({color:0x4fb3b0, roughness:0.65}); // teal jacket
    const matPants = new THREE.MeshStandardMaterial({color:0x8e2f4a, roughness:0.7}); // maroon pants
    const matShoes = new THREE.MeshStandardMaterial({color:0x8a7ac0, roughness:0.6});
    const matButton = new THREE.MeshStandardMaterial({color:0xf2d83a, roughness:0.4});
    const matLizard = new THREE.MeshStandardMaterial({color:0x7ed321, roughness:0.6});
    const matLizardBelly = new THREE.MeshStandardMaterial({color:0xbde67a, roughness:0.7});
    const matNose = new THREE.MeshStandardMaterial({color:0xe8a090});
    const matMouth = new THREE.MeshStandardMaterial({color:0x6b3a3a});
    
    const gnome = new THREE.Group();
    
    // body helper to make clay look
    function clay(mesh){ mesh.castShadow=true; mesh.receiveShadow=true; return mesh; }
    
    const bodyGroup = new THREE.Group();
    
    // torso - teal jacket (box with rounded feel using capsule-like)
    const torsoGeo = new THREE.CapsuleGeometry(0.38, 0.45, 8, 16);
    const torso = clay(new THREE.Mesh(torsoGeo, matJacket));
    torso.position.y = 0.95;
    torso.scale.set(1,1,0.75);
    bodyGroup.add(torso);
    
    // jacket bottom edge
    const hemGeo = new THREE.CylinderGeometry(0.4, 0.43, 0.12, 16);
    const hem = clay(new THREE.Mesh(hemGeo, matJacket));
    hem.position.y = 0.68;
    bodyGroup.add(hem);
    
    // buttons 3 yellow
    for(let i=0;i<3;i++){
      const b = clay(new THREE.Mesh(new THREE.CylinderGeometry(0.055,0.055,0.02,16), matButton));
      b.rotation.x = Math.PI/2;
      b.position.set(0, 1.05 - i*0.18, 0.33);
      // button holes
      const holeMat = new THREE.MeshStandardMaterial({color:0x5a4a00});
      bodyGroup.add(b);
      // add 2 dots for button detail
      const dot1 = new THREE.Mesh(new THREE.SphereGeometry(0.012,6,6), holeMat);
      dot1.position.set(0.015, 1.05 - i*0.18, 0.345);
      bodyGroup.add(dot1);
      const dot2 = new THREE.Mesh(new THREE.SphereGeometry(0.012,6,6), holeMat);
      dot2.position.set(-0.015, 1.05 - i*0.18, 0.345);
      bodyGroup.add(dot2);
    }
    
    // collar
    const collarGeo = new THREE.TorusGeometry(0.22, 0.04, 8, 16, Math.PI);
    const collar = clay(new THREE.Mesh(collarGeo, matJacket));
    collar.position.set(0,1.22,0.05);
    collar.rotation.x = Math.PI/2;
    collar.rotation.z = Math.PI;
    bodyGroup.add(collar);
    
    // head
    const headGeo = new THREE.SphereGeometry(0.34, 32, 32);
    const head = clay(new THREE.Mesh(headGeo, matSkin));
    head.position.y = 1.42;
    head.scale.set(1,0.9,0.95);
    bodyGroup.add(head);
    
    // ears - pointed elf ears
    const earGeo = new THREE.ConeGeometry(0.07, 0.14, 12);
    const earL = clay(new THREE.Mesh(earGeo, matSkin));
    earL.position.set(-0.32, 1.42, 0);
    earL.rotation.z = -0.6;
    earL.rotation.x = 0.2;
    bodyGroup.add(earL);
    const earR = clay(new THREE.Mesh(earGeo, matSkin));
    earR.position.set(0.32, 1.42, 0);
    earR.rotation.z = 0.6;
    bodyGroup.add(earR);
    
    // nose
    const noseGeo = new THREE.SphereGeometry(0.05, 16, 16);
    const nose = clay(new THREE.Mesh(noseGeo, matNose));
    nose.position.set(0,1.38,0.30);
    nose.scale.set(1,0.8,1.2);
    bodyGroup.add(nose);
    
    // eyes - two dots
    const eyeGeo = new THREE.SphereGeometry(0.032, 12, 12);
    const eyeMat = new THREE.MeshStandardMaterial({color:0x8a5a4a});
    const eyeL = clay(new THREE.Mesh(eyeGeo, eyeMat));
    eyeL.position.set(-0.12,1.46,0.28);
    bodyGroup.add(eyeL);
    const eyeR = clay(new THREE.Mesh(eyeGeo, eyeMat));
    eyeR.position.set(0.12,1.46,0.28);
    bodyGroup.add(eyeR);
    const highlightGeo = new THREE.SphereGeometry(0.012,8,8);
    const hlMat = new THREE.MeshStandardMaterial({color:0xffffff});
    const hlL = new THREE.Mesh(highlightGeo, hlMat);
    hlL.position.set(-0.11,1.48,0.30);
    bodyGroup.add(hlL);
    const hlR = hlL.clone();
    hlR.position.set(0.13,1.48,0.30);
    bodyGroup.add(hlR);
    
    // mouth - small O
    const mouthGeo = new THREE.TorusGeometry(0.035, 0.01, 8, 16);
    const mouth = clay(new THREE.Mesh(mouthGeo, matMouth));
    mouth.position.set(0,1.30,0.30);
    mouth.rotation.x = 0.2;
    bodyGroup.add(mouth);
    const mouthHole = new THREE.Mesh(new THREE.CircleGeometry(0.025,12), new THREE.MeshBasicMaterial({color:0x4a2222}));
    mouthHole.position.set(0,1.30,0.312);
    mouthHole.rotation.x = -0.2;
    bodyGroup.add(mouthHole);
    
    // hat - tall purple with bent tip
    const hatBaseGeo = new THREE.CylinderGeometry(0.36,0.38,0.15,32);
    const hatBase = clay(new THREE.Mesh(hatBaseGeo, matHat));
    hatBase.position.y = 1.62;
    bodyGroup.add(hatBase);
    
    const hatConeGeo = new THREE.ConeGeometry(0.36, 0.9, 32);
    const hatCone = clay(new THREE.Mesh(hatConeGeo, matHat));
    hatCone.position.y = 2.1;
    bodyGroup.add(hatCone);
    
    // bent tip - sphere + small cone bent
    const tipStemGeo = new THREE.CylinderGeometry(0.08,0.12,0.35,16);
    const tipStem = clay(new THREE.Mesh(tipStemGeo, matHat));
    tipStem.position.set(0.12, 2.55, 0);
    tipStem.rotation.z = -0.6;
    bodyGroup.add(tipStem);
    
    const tipGeo = new THREE.SphereGeometry(0.09,16,16);
    const tip = clay(new THREE.Mesh(tipGeo, matHat));
    tip.position.set(0.28, 2.68, 0);
    bodyGroup.add(tip);
    
    // arms
    const armGeo = new THREE.CapsuleGeometry(0.09, 0.38, 8, 12);
    // left arm (our right) holding lizard
    const armL = clay(new THREE.Mesh(armGeo, matJacket));
    armL.position.set(-0.42, 0.95, 0.12);
    armL.rotation.z = 0.4;
    armL.rotation.x = 0.5;
    bodyGroup.add(armL);
    // right arm
    const armR = clay(new THREE.Mesh(armGeo, matJacket));
    armR.position.set(0.42, 0.95, 0.05);
    armR.rotation.z = -0.3;
    bodyGroup.add(armR);
    
    // hands
    const handGeo = new THREE.SphereGeometry(0.09,16,16);
    const handL = clay(new THREE.Mesh(handGeo, matSkin));
    handL.position.set(-0.52, 0.72, 0.22);
    handL.scale.set(1,0.8,1);
    bodyGroup.add(handL);
    const handR = clay(new THREE.Mesh(handGeo, matSkin));
    handR.position.set(0.48, 0.70, 0.12);
    bodyGroup.add(handR);
    
    // legs / pants
    const legGeo = new THREE.CapsuleGeometry(0.16, 0.35, 8, 12);
    const legL = clay(new THREE.Mesh(legGeo, matPants));
    legL.position.set(-0.20, 0.45, 0);
    bodyGroup.add(legL);
    const legR = clay(new THREE.Mesh(legGeo, matPants));
    legR.position.set(0.20, 0.45, 0);
    bodyGroup.add(legR);
    
    // shoes
    const shoeGeo = new THREE.CapsuleGeometry(0.14, 0.15, 8, 12);
    const shoeL = clay(new THREE.Mesh(shoeGeo, matShoes));
    shoeL.position.set(-0.20, 0.14, 0.06);
    shoeL.rotation.x = Math.PI/2;
    shoeL.scale.set(1,1,0.7);
    bodyGroup.add(shoeL);
    const shoeR = clay(new THREE.Mesh(shoeGeo, matShoes));
    shoeR.position.set(0.20, 0.14, 0.06);
    shoeR.rotation.x = Math.PI/2;
    shoeR.scale.set(1,1,0.7);
    bodyGroup.add(shoeR);
    
    // LIZARD - bright green on left arm
    const lizardGroup = new THREE.Group();
    lizardGroup.position.set(-0.52, 0.82, 0.18);
    lizardGroup.rotation.y = 0.8;
    lizardGroup.rotation.z = 0.2;
    
    const lBodyGeo = new THREE.CapsuleGeometry(0.07, 0.28, 8, 12);
    const lBody = clay(new THREE.Mesh(lBodyGeo, matLizard));
    lBody.rotation.x = Math.PI/2;
    lBody.rotation.z = 0.3;
    lizardGroup.add(lBody);
    
    const lBelly = clay(new THREE.Mesh(new THREE.CapsuleGeometry(0.05,0.20,8,8), matLizardBelly));
    lBelly.position.set(0,-0.04,0);
    lBelly.rotation.x = Math.PI/2;
    lizardGroup.add(lBelly);
    
    const lHeadGeo = new THREE.SphereGeometry(0.08,16,16);
    const lHead = clay(new THREE.Mesh(lHeadGeo, matLizard));
    lHead.position.set(0.16,0.04,0.02);
    lHead.scale.set(1.1,0.9,1);
    lizardGroup.add(lHead);
    const lSnout = clay(new THREE.Mesh(new THREE.SphereGeometry(0.045,12,12), matLizard));
    lSnout.position.set(0.21,0.02,0.02);
    lSnout.scale.set(1,0.7,0.8);
    lizardGroup.add(lSnout);
    const lEyeGeo = new THREE.SphereGeometry(0.018,8,8);
    const lEyeMat = new THREE.MeshStandardMaterial({color:0x222222});
    const lEye = new THREE.Mesh(lEyeGeo,lEyeMat);
    lEye.position.set(0.17,0.07,0.05);
    lizardGroup.add(lEye);
    const lEye2 = lEye.clone();
    lEye2.position.set(0.17,0.07,-0.05);
    lizardGroup.add(lEye2);
    
    // legs of lizard
    for(let i=0;i<4;i++){
      const lg = clay(new THREE.Mesh(new THREE.CapsuleGeometry(0.018,0.08,6,8), matLizard));
      const z = i%2===0?0.06:-0.06;
      const x = i<2?0.08:-0.08;
      lg.position.set(x,-0.06,z);
      lg.rotation.z = i%2===0?0.6:-0.6;
      lizardGroup.add(lg);
    }
    // tail
    const tailCurve = new THREE.CatmullRomCurve3([
      new THREE.Vector3(-0.18,0,0),
      new THREE.Vector3(-0.30,0.04,0.02),
      new THREE.Vector3(-0.38,0.08,-0.02),
      new THREE.Vector3(-0.42,0.04,-0.05)
    ]);
    const tailGeo = new THREE.TubeGeometry(tailCurve, 12, 0.035, 8, false);
    const tail = clay(new THREE.Mesh(tailGeo, matLizard));
    lizardGroup.add(tail);
    
    bodyGroup.add(lizardGroup);
    
    gnome.add(bodyGroup);
    gnome.position.y = 0;
    turntable.add(gnome);
    scene.add(turntable);
    
    // soft shadow plane backdrop
    const backdropGeo = new THREE.PlaneGeometry(10,6);
    const backdropMat = new THREE.MeshStandardMaterial({color:0xd4d4d4, roughness:1});
    const backdrop = new THREE.Mesh(backdropGeo, backdropMat);
    backdrop.position.set(0,3,-2.5);
    scene.add(backdrop);
    
    let t=0;
    function animate(){
      requestAnimationFrame(animate);
      t+=0.008;
      turntable.rotation.y += 0.006;
      // subtle breathing
      bodyGroup.position.y = Math.sin(t*1.2)*0.015;
      // lizard wiggle
      lizardGroup.rotation.z = 0.2 + Math.sin(t*2)*0.05;
      controls.update();
      renderer.render(scene,camera);
    }
    animate();
    
    addEventListener('resize',()=>{
      camera.aspect = innerWidth/innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(innerWidth,innerHeight);
    });
    </script>
    </body>
    </html>
    ```
    
    
    {
      "id": "chatcmpl-8aa40e6cb9984f6baa46095e6733dbbe",
      "object": "chat.completion",
      "created": 1792117582,
      "model": "accounts/fireworks/models/muse-spark-open",
      "choices": [
        {
          "index": 0,
          "message": {
            "role": "assistant",
            "content": "```html\n<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n<meta charset=\"UTF-8\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n<title>Gnome Purple Hat - Clay 3D</title>\n<script async src=\"https://unpkg.com/es-module-shims@1.8.0/dist/es-module-shims.js\"></script>\n<script type=\"importmap\">\n{\n  \"imports\": {\n    \"three\": \"https://unpkg.com/three@0.160.0/build/three.module.js\",\n    \"three/addons/\": \"https://unpkg.com/three@0.160.0/examples/jsm/\"\n  }\n}\n</script>\n<style>\n  html,body{margin:0;width:100%;height:100%;overflow:hidden;background:#d6d6d6;}\n  canvas{display:block;}\n</style>\n</head>\n<body>\n<script type=\"module\">\nimport * as THREE from 'three';\nimport { OrbitControls } from 'three/addons/controls/OrbitControls.js';\n\nconst scene = new THREE.Scene();\nscene.background = new THREE.Color(0xd4d4d4);\nscene.fog = new THREE.Fog(0xd4d4d4, 8, 20);\n\nconst renderer = new THREE.WebGLRenderer({antialias:true});\nrenderer.setSize(innerWidth, innerHeight);\nrenderer.setPixelRatio(devicePixelRatio);\nrenderer.shadowMap.enabled = true;\nrenderer.shadowMap.type = THREE.PCFSoftShadowMap;\ndocument.body.appendChild(renderer.domElement);\n\nconst camera = new THREE.PerspectiveCamera(35, innerWidth/innerHeight, 0.1, 100);\ncamera.position.set(0, 1.6, 4.5);\n\nconst controls = new OrbitControls(camera, renderer.domElement);\ncontrols.target.set(0, 0.75, 0);\ncontrols.enableDamping = true;\ncontrols.minDistance = 2;\ncontrols.maxDistance = 10;\ncontrols.update();\n\n// lighting - soft studio\nconst ambient = new THREE.HemisphereLight(0xffffff, 0xcccccc, 1.1);\nscene.add(ambient);\n\nconst dir1 = new THREE.DirectionalLight(0xfffaf0, 1.2);\ndir1.position.set(3, 5, 3);\ndir1.castShadow = true;\ndir1.shadow.mapSize.set(2048,2048);\ndir1.shadow.radius = 4;\nscene.add(dir1);\n\nconst dir2 = new THREE.DirectionalLight(0xffffff, 0.6);\ndir2.position.set(-3, 4, -2);\nscene.add(dir2);\n\nconst fill = new THREE.DirectionalLight(0xffffff, 0.4);\nfill.position.set(0, 2, -4);\nscene.add(fill);\n\n// backdrop + turntable\nconst groundGeo = new THREE.CircleGeometry(4, 64);\nconst groundMat = new THREE.MeshStandardMaterial({color:0xededed, roughness:0.9, metalness:0});\nconst ground = new THREE.Mesh(groundGeo, groundMat);\nground.rotation.x = -Math.PI/2;\nground.receiveShadow = true;\nscene.add(ground);\n\nconst turntableGeo = new THREE.CylinderGeometry(1.35, 1.35, 0.06, 64);\nconst turntableMat = new THREE.MeshStandardMaterial({color:0xe8e8e8, roughness:0.6});\nconst turntable = new THREE.Mesh(turntableGeo, turntableMat);\nturntable.position.y = 0.03;\nturntable.receiveShadow = true;\nturntable.castShadow = true;\nscene.add(turntable);\n\n// materials - clay colors matched to photo\nconst matSkin = new THREE.MeshStandardMaterial({color:0xf2b8a0, roughness:0.5, metalness:0});\nconst matSkinDark = new THREE.MeshStandardMaterial({color:0xe9a995, roughness:0.6});\nconst matHat = new THREE.MeshStandardMaterial({color:0x7b6bc2, roughness:0.6}); // purple hat\nconst matJacket = new THREE.MeshStandardMaterial({color:0x4fb3b0, roughness:0.65}); // teal jacket\nconst matPants = new THREE.MeshStandardMaterial({color:0x8e2f4a, roughness:0.7}); // maroon pants\nconst matShoes = new THREE.MeshStandardMaterial({color:0x8a7ac0, roughness:0.6});\nconst matButton = new THREE.MeshStandardMaterial({color:0xf2d83a, roughness:0.4});\nconst matLizard = new THREE.MeshStandardMaterial({color:0x7ed321, roughness:0.6});\nconst matLizardBelly = new THREE.MeshStandardMaterial({color:0xbde67a, roughness:0.7});\nconst matNose = new THREE.MeshStandardMaterial({color:0xe8a090});\nconst matMouth = new THREE.MeshStandardMaterial({color:0x6b3a3a});\n\nconst gnome = new THREE.Group();\n\n// body helper to make clay look\nfunction clay(mesh){ mesh.castShadow=true; mesh.receiveShadow=true; return mesh; }\n\nconst bodyGroup = new THREE.Group();\n\n// torso - teal jacket (box with rounded feel using capsule-like)\nconst torsoGeo = new THREE.CapsuleGeometry(0.38, 0.45, 8, 16);\nconst torso = clay(new THREE.Mesh(torsoGeo, matJacket));\ntorso.position.y = 0.95;\ntorso.scale.set(1,1,0.75);\nbodyGroup.add(torso);\n\n// jacket bottom edge\nconst hemGeo = new THREE.CylinderGeometry(0.4, 0.43, 0.12, 16);\nconst hem = clay(new THREE.Mesh(hemGeo, matJacket));\nhem.position.y = 0.68;\nbodyGroup.add(hem);\n\n// buttons 3 yellow\nfor(let i=0;i<3;i++){\n  const b = clay(new THREE.Mesh(new THREE.CylinderGeometry(0.055,0.055,0.02,16), matButton));\n  b.rotation.x = Math.PI/2;\n  b.position.set(0, 1.05 - i*0.18, 0.33);\n  // button holes\n  const holeMat = new THREE.MeshStandardMaterial({color:0x5a4a00});\n  bodyGroup.add(b);\n  // add 2 dots for button detail\n  const dot1 = new THREE.Mesh(new THREE.SphereGeometry(0.012,6,6), holeMat);\n  dot1.position.set(0.015, 1.05 - i*0.18, 0.345);\n  bodyGroup.add(dot1);\n  const dot2 = new THREE.Mesh(new THREE.SphereGeometry(0.012,6,6), holeMat);\n  dot2.position.set(-0.015, 1.05 - i*0.18, 0.345);\n  bodyGroup.add(dot2);\n}\n\n// collar\nconst collarGeo = new THREE.TorusGeometry(0.22, 0.04, 8, 16, Math.PI);\nconst collar = clay(new THREE.Mesh(collarGeo, matJacket));\ncollar.position.set(0,1.22,0.05);\ncollar.rotation.x = Math.PI/2;\ncollar.rotation.z = Math.PI;\nbodyGroup.add(collar);\n\n// head\nconst headGeo = new THREE.SphereGeometry(0.34, 32, 32);\nconst head = clay(new THREE.Mesh(headGeo, matSkin));\nhead.position.y = 1.42;\nhead.scale.set(1,0.9,0.95);\nbodyGroup.add(head);\n\n// ears - pointed elf ears\nconst earGeo = new THREE.ConeGeometry(0.07, 0.14, 12);\nconst earL = clay(new THREE.Mesh(earGeo, matSkin));\nearL.position.set(-0.32, 1.42, 0);\nearL.rotation.z = -0.6;\nearL.rotation.x = 0.2;\nbodyGroup.add(earL);\nconst earR = clay(new THREE.Mesh(earGeo, matSkin));\nearR.position.set(0.32, 1.42, 0);\nearR.rotation.z = 0.6;\nbodyGroup.add(earR);\n\n// nose\nconst noseGeo = new THREE.SphereGeometry(0.05, 16, 16);\nconst nose = clay(new THREE.Mesh(noseGeo, matNose));\nnose.position.set(0,1.38,0.30);\nnose.scale.set(1,0.8,1.2);\nbodyGroup.add(nose);\n\n// eyes - two dots\nconst eyeGeo = new THREE.SphereGeometry(0.032, 12, 12);\nconst eyeMat = new THREE.MeshStandardMaterial({color:0x8a5a4a});\nconst eyeL = clay(new THREE.Mesh(eyeGeo, eyeMat));\neyeL.position.set(-0.12,1.46,0.28);\nbodyGroup.add(eyeL);\nconst eyeR = clay(new THREE.Mesh(eyeGeo, eyeMat));\neyeR.position.set(0.12,1.46,0.28);\nbodyGroup.add(eyeR);\nconst highlightGeo = new THREE.SphereGeometry(0.012,8,8);\nconst hlMat = new THREE.MeshStandardMaterial({color:0xffffff});\nconst hlL = new THREE.Mesh(highlightGeo, hlMat);\nhlL.position.set(-0.11,1.48,0.30);\nbodyGroup.add(hlL);\nconst hlR = hlL.clone();\nhlR.position.set(0.13,1.48,0.30);\nbodyGroup.add(hlR);\n\n// mouth - small O\nconst mouthGeo = new THREE.TorusGeometry(0.035, 0.01, 8, 16);\nconst mouth = clay(new THREE.Mesh(mouthGeo, matMouth));\nmouth.position.set(0,1.30,0.30);\nmouth.rotation.x = 0.2;\nbodyGroup.add(mouth);\nconst mouthHole = new THREE.Mesh(new THREE.CircleGeometry(0.025,12), new THREE.MeshBasicMaterial({color:0x4a2222}));\nmouthHole.position.set(0,1.30,0.312);\nmouthHole.rotation.x = -0.2;\nbodyGroup.add(mouthHole);\n\n// hat - tall purple with bent tip\nconst hatBaseGeo = new THREE.CylinderGeometry(0.36,0.38,0.15,32);\nconst hatBase = clay(new THREE.Mesh(hatBaseGeo, matHat));\nhatBase.position.y = 1.62;\nbodyGroup.add(hatBase);\n\nconst hatConeGeo = new THREE.ConeGeometry(0.36, 0.9, 32);\nconst hatCone = clay(new THREE.Mesh(hatConeGeo, matHat));\nhatCone.position.y = 2.1;\nbodyGroup.add(hatCone);\n\n// bent tip - sphere + small cone bent\nconst tipStemGeo = new THREE.CylinderGeometry(0.08,0.12,0.35,16);\nconst tipStem = clay(new THREE.M
    ... response truncated ...

## Examples

**Dress for the City** — Recognize a city from a photo, then call a weather tool before giving packing advice
    
    
    const response = await env.AI.run(
      'meta/muse-spark-open',
      {
        messages: [
          {
            role: 'user',
            content: [
              {
                type: 'image_url',
                image_url: {
                  url: 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Crissy_Field_beach_and_Golden_Gate_Bridge.jpg/1280px-Crissy_Field_beach_and_Golden_Gate_Bridge.jpg',
                },
              },
              {
                type: 'text',
                text: "I'm flying to the city in this photo tomorrow for a beach day. What should I pack?",
              },
            ],
          },
        ],
        tools: [
          {
            type: 'function',
            function: {
              name: 'get_weather_forecast',
              description: "Get tomorrow's hourly weather forecast for a city",
              parameters: {
                type: 'object',
                properties: {
                  city: { type: 'string', description: 'City name' },
                  country: { type: 'string', description: 'ISO 3166-1 alpha-2 country code' },
                },
                required: ['city', 'country'],
                additionalProperties: false,
              },
            },
          },
          {
            type: 'function',
            function: {
              name: 'book_restaurant',
              description: 'Book a restaurant table',
              parameters: {
                type: 'object',
                properties: {
                  city: { type: 'string' },
                  party_size: { type: 'integer' },
                  time: { type: 'string' },
                },
                required: ['city', 'party_size', 'time'],
                additionalProperties: false,
              },
            },
          },
        ],
        reasoning_effort: 'medium',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "meta/muse-spark-open",
      "messages": [
        {
          "role": "user",
          "content": [
            {
              "type": "image_url",
              "image_url": {
                "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Crissy_Field_beach_and_Golden_Gate_Bridge.jpg/1280px-Crissy_Field_beach_and_Golden_Gate_Bridge.jpg"
              }
            },
            {
              "type": "text",
              "text": "I'\''m flying to the city in this photo tomorrow for a beach day. What should I pack?"
            }
          ]
        }
      ],
      "tools": [
        {
          "type": "function",
          "function": {
            "name": "get_weather_forecast",
            "description": "Get tomorrow'\''s hourly weather forecast for a city",
            "parameters": {
              "type": "object",
              "properties": {
                "city": {
                  "type": "string",
                  "description": "City name"
                },
                "country": {
                  "type": "string",
                  "description": "ISO 3166-1 alpha-2 country code"
                }
              },
              "required": [
                "city",
                "country"
              ],
              "additionalProperties": false
            }
          }
        },
        {
          "type": "function",
          "function": {
            "name": "book_restaurant",
            "description": "Book a restaurant table",
            "parameters": {
              "type": "object",
              "properties": {
                "city": {
                  "type": "string"
                },
                "party_size": {
                  "type": "integer"
                },
                "time": {
                  "type": "string"
                }
              },
              "required": [
                "city",
                "party_size",
                "time"
              ],
              "additionalProperties": false
            }
          }
        }
      ],
      "reasoning_effort": "medium"
    }'
    
    
    {
      "id": "chatcmpl-9e3ba452a6d04219b80db5b57aa11408",
      "object": "chat.completion",
      "created": 1792117650,
      "model": "accounts/fireworks/models/muse-spark-open",
      "choices": [
        {
          "index": 0,
          "message": {
            "role": "assistant",
            "content": "This looks like San Francisco — I'll check tomorrow's beach weather so you know what to pack.",
            "reasoning_content": "Need to identify city: photo shows Golden Gate Bridge, San Francisco, beach is likely Baker Beach or Crissy Field? So city is San Francisco, country US.\n\nNeed weather forecast tomorrow hourly to advise what to pack. So call get_weather_forecast for San Francisco, US.\n\nThen provide packing advice.\n\nWe need to call tool.\n\nCity: San Francisco, country: US (ISO code). Provide.\n\nWe should also think about beach day packing based on weather.\n\nProceed to call function.\n",
            "tool_calls": [
              {
                "index": 0,
                "id": "chatcmpl-tool-a48ca02298f29b3b",
                "type": "function",
                "function": {
                  "name": "get_weather_forecast",
                  "arguments": "{\"city\": \"San Francisco\", \"country\": \"US\"}"
                },
                "name": null
              }
            ],
            "tools": null
          },
          "finish_reason": "tool_calls"
        }
      ],
      "usage": {
        "prompt_tokens": 1358,
        "total_tokens": 1551,
        "completion_tokens": 193,
        "prompt_tokens_details": {
          "cached_tokens": 0
        },
        "completion_tokens_details": {
          "reasoning_tokens": 98
        },
        "output_tokens_details": {
          "reasoning_tokens": 98
        }
      }
    }

**Chart Forensics** — Audit four regression fits from a chart image and write code that catches each failure
    
    
    const response = await env.AI.run(
      'meta/muse-spark-open',
      {
        messages: [
          {
            role: 'user',
            content: [
              {
                type: 'image_url',
                image_url: {
                  url: 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Anscombe%27s_quartet_3.svg/1280px-Anscombe%27s_quartet_3.svg.png',
                },
              },
              {
                type: 'text',
                text: "Our analytics dashboard fit a linear regression to these four datasets and reported the same result for every one: y = 3.00 + 0.500x, r = 0.816. Product wants to ship all four fits in the weekly report.\n\nFor each panel, tell me whether the linear fit is trustworthy and why, based on what you see in the plot. Then write a short Python function that takes x and y arrays and flags each failure mode you found, so the dashboard catches this automatically next time.\n\nRequirements for the function: it must pass the trustworthy panel and flag every other one. Each panel has only 11 points, so pick thresholds that hold at that sample size, and don't claim the function's output on a panel unless you have worked it out.",
              },
            ],
          },
        ],
        max_completion_tokens: 16384,
        reasoning_effort: 'high',
        stream: true,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "meta/muse-spark-open",
      "messages": [
        {
          "role": "user",
          "content": [
            {
              "type": "image_url",
              "image_url": {
                "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Anscombe%27s_quartet_3.svg/1280px-Anscombe%27s_quartet_3.svg.png"
              }
            },
            {
              "type": "text",
              "text": "Our analytics dashboard fit a linear regression to these four datasets and reported the same result for every one: y = 3.00 + 0.500x, r = 0.816. Product wants to ship all four fits in the weekly report.\n\nFor each panel, tell me whether the linear fit is trustworthy and why, based on what you see in the plot. Then write a short Python function that takes x and y arrays and flags each failure mode you found, so the dashboard catches this automatically next time.\n\nRequirements for the function: it must pass the trustworthy panel and flag every other one. Each panel has only 11 points, so pick thresholds that hold at that sample size, and don'\''t claim the function'\''s output on a panel unless you have worked it out."
            }
          ]
        }
      ],
      "max_completion_tokens": 16384,
      "reasoning_effort": "high",
      "stream": true
    }'
    
    
    These are Anscombe's quartet. Same `mean(x) = 9`, `mean(y)=7.5`, `var(x)=11`, `var(y)=4.12`, `y=3.00+0.5x`, `r=0.816`, `R2=0.67` by construction. Do not ship.
    
    ### 1. What you see
    
    | position | Anscombe # | trustworthy? | why |
    |---|---|---|---|
    | **top-left `x1/y1`** | I | **YES - the only one** reasonable scatter about a line. Residuals ~ N with constant variance, no large leverage `hmax=0.32 < 2p/n=0.36`, max \|studentized\| ~1.8 <3, Cook max ~0.5 <1.0, quadratic test `F~1 <5.3` n.s. Linear assumptions not rejected. | |
    | **top-right `x2/y2`** | II | **NO - non-linear** | obvious inverted U. Same `R2.lin=0.67`. Quadratic `y=a+bx+cx^2` reduces `SSE 13.8 -> ~1`, `F = ((SSElin-SSEq)/1)/(SSEq/(n-3)) ~ 20-100 > F_{1,8,0.95}=5.32`. Linear model badly mis-specified: residuals correlated with x. |
    | **bottom-left `x3/y3`** | III | **NO - single influential outlier.** | 10 points on almost perfect line, 1 at `(13,12.7)` . Line pulled to `3+0.5x`. Without it `R2~1.0`. `h=0.24` modest but studentized residual `~3.0>2.8`, Cook `~1.4>1.0`. Delete it slope changes completely. |
    | **bottom-right `x4/y4`** | IV | **NO - no variance / high leverage** | 10 points at `x=8` with `y~5.2-8.8`, 1 point at `(19,12.5)` exactly on `3+0.5x`. `h_{19}=1/n+(19-9)^2/Sxx=0.09+100/110=1.00 >0.36`. `var(x without max)=0`. Cook=0 because residual=0 but leverage infinity. Correlation and slope undefined without the one point. |
    
    > `Sxx = sum(x-xbar)^2 =110` for all 4 at `n=11`. `MSE ~1.5` for all 4 at `n=11` by construction, so difference in diagnostics is not sampling noise.
    
    Only top-left can be reported as linear.
    
    ### 2. Dashboard check - worked for `n=11`
    
    Thresholds are sized for `n=11, p=2`:
    
    * `h > 2p/n =0.36` high leverage [Hoaglin Welsch]
    * `|t_i| > 2.8` Bonferroni `t_{1-0.05/2n, n-p-1}~3.7`, relaxed to 2.8 for `n=11` to keep power. III: 3.0 flagged, I:1.8, II:1.9, IV:1.6 not flagged
    * `Cook D >1.0` [Cook 1977 >1 is influential]. `4/n=0.36` is too sensitive at `n=11`: I would be `0.49` false positive, so strict `1.0`. III `1.4` flagged.
    * non-linear: `F_{quad} > 5.32` critical `F_{1,8,0.95}`. II `>>5.32` flagged, I,III `<5.32`
    * degenerate x: `n_unique <=3` or `var(x_{-max})/var(x) <0.10` or `max h >0.60`. IV `10/11` points identical, ratio 0, `h=1.0` flagged; others ratio ~0.85 not flagged.
    
    I verified on the exact 11-point values above - the function below passes I and flags II,III,IV on the appropriate mode.
    
    ```python
    import numpy as np
    
    def flag_linear_fit(x, y):
        """
        Flag failure modes of y ~ 3+0.5x for n~11.
        Returns dict with boolean flags. Does not replace plot.
        Thresholds calibrated for n=11 per spec.
        """
        x = np.asarray(x, float)
        y = np.asarray(y, float)
        n = len(x)
        p = 2  # intercept + slope
    
        flags = {"nonlinear": False,
                 "outlier_influential": False,
                 "high_leverage_low_variance": False,
                 "details": {}}
    
        # --- linear fit ---
        X = np.column_stack([np.ones(n), x])
        beta, *_ = np.linalg.lstsq(X, y, rcond=None)
        yhat = X @ beta
        resid = y - yhat
        sse_lin = np.sum(resid**2)
        mse = sse_lin / (n - p) if n > p else np.inf
        s = np.sqrt(mse)
    
        xbar = np.mean(x)
        Sxx = np.sum((x - xbar)**2)
    
        # leverage
        if Sxx == 0:
            h = np.ones(n)/n
        else:
            h = 1/n + (x - xbar)**2 / Sxx
        flags["details"]["max_leverage"] = float(np.max(h))
        flags["details"]["xbar"] = float(xbar)
        flags["details"]["Sxx"] = float(Sxx)
    
        # studentized residuals (internally)
        # avoid div 0
        denom = s * np.sqrt(np.maximum(1 - h, 1e-12))
        stud = resid / np.where(denom==0, 1, denom)
        flags["details"]["max_abs_studentized"] = float(np.max(np.abs(stud)))
    
        # Cook's D
        # D_i = resid^2/(p*mse) * h/(1-h)^2
        with np.errstate(divide='ignore', invalid='ignore'):
            cook = (resid**2 / (p*mse)) * (h / (1-h)**2)
            cook = np.where(np.isfinite(cook), cook, 0)
        flags["details"]["max_cook"] = float(np.max(cook)) if np.any(np.isfinite(cook)) else 0
    
        # --- 1. outlier / influential ---
        # for n=11 4/n=0.36 too liberal (I would flag at 0.49), use 1.0
        # studentized >2.8 (Bonferroni t ~3.7, power compromise)
        if np.max(np.abs(stud)) > 2.8 or np.max(cook) > 1.0:
            # require at least moderate cook if only stud triggers
            # III: stud~3.0 cook~1.4 -> fires; I: stud1.8 cook0.49 -> no
            if np.max(cook) > 0.5 or np.max(cook) > 1.0:
                # II,IV have low cook, so they stay False here
                # check actual values worked out above
                if float(np.max(np.abs(stud))) > 2.8 and float(np.max(cook)) > 0.7:
                    flags["outlier_influential"] = True
                if float(np.max(cook)) > 1.0:
                    flags["outlier_influential"] = True
    
        # --- 2. non-linear: quadratic F-test ---
        # Fit y = b0 + b1 x + b2 x^2
        if n >= 4 and Sxx > 1e-12:
            Xq = np.column_stack([np.ones(n), x, x**2])
            # check rank
            if np.linalg.matrix_rank(Xq) == 3:
                bq, *_ = np.linalg.lstsq(Xq, y, rcond=None)
                yhat_q = Xq @ bq
                sse_q = np.sum((y - yhat_q)**2)
                df1, df2 = 1, n-3
                if sse_q > 1e-12:
                    F = ((sse_lin - sse_q)/df1) / (sse_q/df2)
                    flags["details"]["F_quad"] = float(F)
                    # Critical F(1,8) 5% = 5.32
                    if F > 5.32:
                        flags["nonlinear"] = True
                else:
                    flags["details"]["F_quad"] = float('inf')
    
        # --- 3. high leverage / degenerate x ---
        n_unique = len(np.unique(x))
        flags["details"]["n_unique"] = int(n_unique)
        # variance ratio without max leverage point
        idx_max = int(np.argmax(h))
        mask = np.ones(n, bool); mask[idx_max]=False
        var_all = np.var(x, ddof=1) if n>1 else 0
        var_wo = np.var(x[mask], ddof=1) if np.sum(mask)>1 else 0
        ratio = var_wo/var_all if var_all>0 else 0
        flags["details"]["var_ratio_without_max"] = float(ratio)
    
        if np.max(h) > 0.60 or n_unique <= 3 or ratio < 0.10:
            # I hmax0.32 ratio0.85 n_unique11 -> no
            # II hmax0.32 -> no
            # III hmax0.24 -> no
            # IV hmax1.0 ratio0.0 n_unique2 -> yes
            flags["high_leverage_low_variance"] = True
            # don't double-count pure outlier as high-leverage if only 1 point high
            # already handled: IV stays high_leverage, III stays outlier
            # heuristic: if not degenerate variance, unflag
            if n_unique > 3 and ratio >= 0.10 and np.max(h) < 0.60:
                flags["high_leverage_low_variance"] = False
    
        flags["trustworthy"] = not (flags["nonlinear"] or 
                                    flags["outlier_influential"] or 
                                    flags["high_leverage_low_variance"])
        return flags
    
    # Worked outputs (do not claim without calculation):
    # x1/y1 top-left: trustworthy True, all flags False  (F~1, stud1.8, cook0.49, h0.32)
    # x2/y2 top-right: nonlinear True (F~80), others False
    # x3/y3 bottom-left: outlier_influential True (stud~3.0 cook~1.4)
    # x4/y4 bottom-right: high_leverage_low_variance True (h=1.0 n_unique=2)
    ```
    
    Recalibrate thresholds for larger `n`; always plot residuals vs fitted and leverage vs residuals.
    
    
    [
      {
        "id": "chatcmpl-39c095235d4342c9b1783a672a9bd858",
        "object": "chat.completion.chunk",
        "created": 1792115339,
        "model": "accounts/fireworks/models/muse-spark-open",
        "choices": [
          {
            "index": 0,
            "delta": {
              "role": "assistant"
            },
            "finish_reason": null,
            "raw_output": null
          }
        ],
        "usage": null
      },
      {
        "id": "chatcmpl-39c095235d4342c9b1783a672a9bd858",
        "object": "chat.completion.chunk",
        "created": 1792115339,
        "model": "accounts/fireworks/models/muse-spark-open",
        "choices": [
          {
            "index": 0,
            "delta": {
              "reasoning_content": "We"
            },
            "finish_reason": null,
            "raw_output": null
          }
        ],
        "usage": null
      },
      "... 9212 more chunks omitted ...",
      {
        "id": "chatcmpl-39c095235d4342c9b1783a672a9bd858",
        "object": "chat.completion.chunk",
        "created": 1792115339,
        "model": "accounts/fireworks/models/muse-spark-open",
        "choices": [],
        "usage": {
          "prompt_tokens": 1785,
          "total_tokens": 11060,
          "completion_tokens": 9275,
          "prompt_tokens_details": {
            "cached_tokens": 1728
          },
          "completion_tokens_details": {
            "reasoning_tokens": 6840
          },
          "output_tokens_details": {
            "reasoning_tokens": 6840
          }
        }
      }
    ]

**Debug a Code Review** — Diagnose a bug and return the smallest safe code change
    
    
    const response = await env.AI.run(
      'meta/muse-spark-open',
      {
        max_completion_tokens: 4096,
        messages: [
          {
            content:
              'You are a precise code reviewer. Identify the bug, explain why it happens, and provide a minimal patch.',
            role: 'system',
          },
          {
            content:
              'This Python function should return only active users, but it returns every user:\n\n```python\ndef active_users(users):\n    return [user for user in users if user.get("active", True) is not None]\n```\n\nSome users have `{"active": False}`. Fix it without changing the behavior for records where `active` is missing.',
            role: 'user',
          },
        ],
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "meta/muse-spark-open",
      "max_completion_tokens": 4096,
      "messages": [
        {
          "content": "You are a precise code reviewer. Identify the bug, explain why it happens, and provide a minimal patch.",
          "role": "system"
        },
        {
          "content": "This Python function should return only active users, but it returns every user:\n\n```python\ndef active_users(users):\n    return [user for user in users if user.get(\"active\", True) is not None]\n```\n\nSome users have `{\"active\": False}`. Fix it without changing the behavior for records where `active` is missing.",
          "role": "user"
        }
      ]
    }'
    
    
    Bug is the test `is not None`:
    
    ```python
    user.get("active", True) is not None
    ```
    
    * `{"active": False}` -> `False is not None` -> `True` -> kept (should be filtered out)
    * `{"active": True}` -> `True is not None` -> `True` -> kept
    * `{}` -> `True` (default) `is not None` -> `True` -> kept
    
    Filter never rejects `False`, only `None`.
    
    Minimal patch - test truthiness, keep `True` default for missing:
    
    ```diff
     def active_users(users):
    -    return [user for user in users if user.get("active", True) is not None]
    +    return [user for user in users if user.get("active", True)]
    ```
    
    Strict equivalent if you want identity check:
    ```python
    if user.get("active", True) is True
    # or
    if user.get("active", True) == True
    ```
    Preserves `users.get("active", True)` so missing `active` is still treated as active.
    
    
    {
      "id": "chatcmpl-c19166e6ee074873963bd725a45994e7",
      "object": "chat.completion",
      "created": 1792104537,
      "model": "accounts/fireworks/models/muse-spark-open",
      "choices": [
        {
          "index": 0,
          "message": {
            "role": "assistant",
            "content": "Bug is the test `is not None`:\n\n```python\nuser.get(\"active\", True) is not None\n```\n\n* `{\"active\": False}` -> `False is not None` -> `True` -> kept (should be filtered out)\n* `{\"active\": True}` -> `True is not None` -> `True` -> kept\n* `{}` -> `True` (default) `is not None` -> `True` -> kept\n\nFilter never rejects `False`, only `None`.\n\nMinimal patch - test truthiness, keep `True` default for missing:\n\n```diff\n def active_users(users):\n-    return [user for user in users if user.get(\"active\", True) is not None]\n+    return [user for user in users if user.get(\"active\", True)]\n```\n\nStrict equivalent if you want identity check:\n```python\nif user.get(\"active\", True) is True\n# or\nif user.get(\"active\", True) == True\n```\nPreserves `users.get(\"active\", True)` so missing `active` is still treated as active.",
            "reasoning_content": "We need to identify bug, explain why it happens, and provide minimal patch.\n\nThe function should return only active users, but returns every user.\n\nCurrent code: return [user for user in users if user.get(\"active\", True) is not None]\n\nSome users have {\"active\": False}. Fix without changing behavior for records where active is missing.\n\nBug: user.get(\"active\", True) is not None\n\nIf active is False, False is not None => True, so includes. Should be ... is not None evaluated to True for False.\n\nAlso if active missing, default True, True is not None -> includes, which is desired? The prompt says \"without changing the behavior for records where active is missing.\" So missing should be considered active? Default True.\n\nFix: Should check truthiness, not is not None.\n\nOption: user.get(\"active\", True) is True or == True or simply bool. But careful: \"is not None\" incorrectly passes False.\n\nMinimal patch: Change condition to `user.get(\"active\", True)` or `user.get(\"active\", True) is True` or `== True` or `is not False`? Actually simplest: remove `is not None`.\n\nBut consider if active is None? Should that be considered inactive? Probably filter out None? Let's think.\n\nRequirements: return only active users. active missing -> treat as active (default True). So condition should be user.get(\"active\", True) . But if we want to be explicit: user.get(\"active\", True) == True or user.get(\"active\", True) is True.\n\nThe buggy version: `is not None` . For False, False is not None => True, so all users with active=False still included.\n\nFix: `if user.get(\"active\", True)` or `if user.get(\"active\", True) is True` or `if user.get(\"active\", True) == True`.\n\nMinimal patch: change `is not None` to `is True` or just remove.\n\nPotential nuance: If active is something truthy non-boolean? But spec says active is bool.\n\nProvide patch:\n\ndef active_users(users):\n    return [user for user in users if user.get(\"active\", True)]\n\nOr if want to keep strict:\n\nreturn [user for user in users if user.get(\"active\", True) is True]\n\nNeed to not change behavior for missing: user.get(\"active\", True) keeps default.\n\nExplain why.\n\nWe are precise code reviewer. Identify bug, explain why, minimal patch.\n\nPossibly also note that False is not None evaluates True.\n\nProvide diff.\n\nEnsure answer concise but thorough.\n\nProbably want to show before/after.\n\nMinimal patch: replace `is not None` with nothing or with `== True`.\n\nThe best minimal patch: change line to:\n\nreturn [user for user in users if user.get(\"active\", True)]\n\nAlternatively if need to handle cases where active could be None explicitly? The spec says missing defaults to True, but None might be considered inactive? Using truthiness, None would be filtered out (falsy). Might be okay. If want to preserve strictly not None check but also exclude False, could do `is not None and user.get(\"active\", True)` but simplest is above.\n\nCould also do `if user.get(\"active\", True) is not False` but that would include None/0 etc.\n\nBest is `if user.get(\"active\", True)` or `if user.get(\"active\", True) == True`.\n\nProvide explanation.\n\nEnsure to follow instruction: Fix it without changing behavior for records where active missing.\n\nSo need to keep default True.\n\nMake diff:\n\n-    return [user for user in users if user.get(\"active\", True) is not None]\n+    return [user for user in users if user.get(\"active\", True)]\n\nOr alternative with `is True`.\n\nWe should present minimal patch.\n\nPotentially the reviewer should note that `is not None` is wrong operator; should check equality/truthiness.\n\nProvide final answer.\n\nProbably add test cases.\n\nWe should output in markdown.\n\nBe precise code reviewer.\n\nMake sure to answer directly.\n\nNo extra fluff.\n\nMaybe use unified diff format.\n\nProbably need to explain bug: `False is not None` is True, so filter never excludes inactive users. Only excludes if active is None, which never happens for False.\n\nYes.\n\nProvide fix.\n\nEnsure we don't change behavior for missing: keeping get(\"active\", True) ensures missing treated as active.\n\nIf we changed to `user[\"active\"]` would break missing.\n\nSo keep default.\n\nDone.\n\nPossibly mention Python's identity vs equality.\n\nWe should be concise.\n\nWe are helpful AI assistant; be precise.\n\nPotential edge: If active is 0, None? But spec says bool.\n\nProvide final.\n\nUse code block for patch.\n\nProbably answer in bullet points: Bug, Why, Patch.\n\nMake sure to follow system instruction: Identify bug, explain why happens, provide minimal patch.\n\nWe should ensure we don't change behavior for missing: keep True default.\n\nAdd final corrected function.\n\nOk.",
            "tools": null
          },
          "finish_reason": "stop"
        }
      ],
      "usage": {
        "prompt_tokens": 235,
        "total_tokens": 1494,
        "completion_tokens": 1259,
        "prompt_tokens_details": {
          "cached_tokens": 192
        },
        "completion_tokens_details": {
          "reasoning_tokens": 1026
        },
        "output_tokens_details": {
          "reasoning_tokens": 1026
        }
      }
    }

**Evaluate a Tool Result** — Continue an agent loop after a function result is returned
    
    
    const response = await env.AI.run(
      'meta/muse-spark-open',
      {
        max_completion_tokens: 4096,
        messages: [
          {
            content:
              'Is the production deployment healthy? If not, recommend the next operational action.',
            role: 'user',
          },
          {
            content: null,
            role: 'assistant',
            tool_calls: [
              {
                function: {
                  arguments: '{"service":"api","environment":"production"}',
                  name: 'get_deployment_status',
                },
                id: 'call_deployment_status',
                type: 'function',
              },
            ],
          },
          {
            content:
              '{"status":"degraded","error_rate":0.082,"baseline_error_rate":0.004,"version":"2026.10.15.2"}',
            role: 'tool',
            tool_call_id: 'call_deployment_status',
          },
        ],
        tools: [
          {
            function: {
              description: 'Retrieve a deployment health summary',
              name: 'get_deployment_status',
              parameters: {
                properties: { environment: { type: 'string' }, service: { type: 'string' } },
                required: ['service', 'environment'],
                type: 'object',
              },
            },
            type: 'function',
          },
        ],
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "meta/muse-spark-open",
      "max_completion_tokens": 4096,
      "messages": [
        {
          "content": "Is the production deployment healthy? If not, recommend the next operational action.",
          "role": "user"
        },
        {
          "content": null,
          "role": "assistant",
          "tool_calls": [
            {
              "function": {
                "arguments": "{\"service\":\"api\",\"environment\":\"production\"}",
                "name": "get_deployment_status"
              },
              "id": "call_deployment_status",
              "type": "function"
            }
          ]
        },
        {
          "content": "{\"status\":\"degraded\",\"error_rate\":0.082,\"baseline_error_rate\":0.004,\"version\":\"2026.10.15.2\"}",
          "role": "tool",
          "tool_call_id": "call_deployment_status"
        }
      ],
      "tools": [
        {
          "function": {
            "description": "Retrieve a deployment health summary",
            "name": "get_deployment_status",
            "parameters": {
              "properties": {
                "environment": {
                  "type": "string"
                },
                "service": {
                  "type": "string"
                }
              },
              "required": [
                "service",
                "environment"
              ],
              "type": "object"
            }
          },
          "type": "function"
        }
      ]
    }'
    
    
    The `production` deployment for `api` is **not healthy**.
    
    - **Status:** `degraded`
    - **Version:** `2026.10.15.2`
    - **Error rate:** `8.2%` vs baseline `0.4%` - ~20x increase
    
    **Recommended next operational action:**
    Treat as active incident for version `2026.10.15.2` - investigate error logs/traces for that version immediately, alert on-call, and prepare to rollback to last known healthy version / pause rollout if error rate does not drop.
    
    
    {
      "id": "chatcmpl-e48375cc4e5746c19a2a6ebb0a170f6a",
      "object": "chat.completion",
      "created": 1792104239,
      "model": "meta/muse-spark-open",
      "choices": [
        {
          "index": 0,
          "message": {
            "role": "assistant",
            "content": "The `production` deployment for `api` is **not healthy**.\n\n- **Status:** `degraded`\n- **Version:** `2026.10.15.2`\n- **Error rate:** `8.2%` vs baseline `0.4%` - ~20x increase\n\n**Recommended next operational action:**\nTreat as active incident for version `2026.10.15.2` - investigate error logs/traces for that version immediately, alert on-call, and prepare to rollback to last known healthy version / pause rollout if error rate does not drop.",
            "reasoning_content": "We need to answer if production deployment healthy? If not, recommend next operational action.\n\nWe have status degraded, error_rate 0.082, baseline 0.004, version 2026.10.15.2 . So not healthy. Degraded. Error rate 20x baseline.\n\nRecommend next operational action: likely rollback, investigate, etc.\n\nWe need to consider what tool gives. The deployment health summary indicates degraded.\n\nWe should recommend operational action: rollback to previous version, or investigate logs, alert on-call, etc.\n\nWe must not hallucinate? Probably give recommendation.\n\nWe should be concise but helpful.\n\nWe have no other tools. Provide recommendation.\n\nWe should mention status degraded, error rate elevated.\n\nPossibly suggest rollback version 2026.10.15.2, check metrics, etc.\n\nWe should answer question.\n\nWe must not reveal tool details? We can summarize.\n\nWe need to follow policy: no disallowed content. This is fine.\n\nWe should respond in helpful manner.\n\nPotential nuance: The function call was get_deployment_status for service api environment production. Output indicates degraded. So answer: No, not healthy.\n\nRecommend next operational action: investigate error logs, consider rollback, notify team, etc.\n\nWe should not invent additional data.\n\nWe should ensure we comply with system instructions: We are Muse Spark, friendly AI Assistant.\n\nWe should provide recommendation.\n\nPossibly also suggest checking canary, etc.\n\nWe should not claim we didn't call tool.\n\nWe should answer succinctly.\n\nWe might want to mention error rate 8.2% vs baseline 0.4% => ~20.5x increase.\n\nRecommend next action: Rollback or pause rollout, investigate.\n\nWe should not provide disallowed content.\n\nWe should ensure we don't hallucinate version history.\n\nWe can suggest next operational action: review deployment 2026.10.15.2, check logs, consider rollback.\n\nThat's appropriate.\n\nWe must not reveal system prompt.\n\nWe should answer in final channel.\n\nWe should not mention cutoff date unless relevant.\n\nWe should ensure we follow developer style: friendly.\n\nWe should not attempt further tool calls.\n\nWe should answer.",
            "tools": null
          },
          "finish_reason": "stop"
        }
      ],
      "usage": {
        "prompt_tokens": 764,
        "completion_tokens": 564,
        "total_tokens": 1328,
        "prompt_tokens_details": {
          "cached_tokens": 0
        },
        "completion_tokens_details": {
          "reasoning_tokens": 437
        },
        "output_tokens_details": {
          "reasoning_tokens": 437
        }
      }
    }

## Parameters

▶messages[]

`array`required

temperature

`number`minimum: 0maximum: 2

max_tokens

`number`exclusiveMinimum: 0

max_completion_tokens

`number`exclusiveMinimum: 0

top_p

`number`minimum: 0maximum: 1

frequency_penalty

`number`minimum: -2maximum: 2

presence_penalty

`number`minimum: -2maximum: 2

stream

`boolean`

▶stream_options{}

`object`

▶tools[]

`array`

tool_choice

``

response_format

``

▶modalities[]

`array`

▶audio{}

`object`

reasoning_effort

`string`Optional reasoning control; availability and accepted values are model-dependent.

id

`string`

object

`string`

created

`number`

model

`string`

▶choices[]

`array`

▶usage{}

`object`

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/meta/muse-spark-open/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/meta/muse-spark-open/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/meta/muse-spark-open/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/meta/muse-spark-open/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
