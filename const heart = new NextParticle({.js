const heart = new NextParticle({
    renderer: 'webgl',
    image: document.querySelector('#valentines'),
    width: window.innerWidth,
    height: window.innerHeight,
    particlegap: settings.particlegap,
    particleSize: settings.particleSize,
    mouseForce: settings.mouseForce,
    noise: settings.noise,
    layercount: settings.layercount,
    layerDistance: settings.layerDistance,
});