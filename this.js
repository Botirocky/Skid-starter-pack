this.init = function() {
    this.x = Math.cos(this.source.angle)
    this.y = Math.sin(this.source.angle)
    this.x = this.x + (canvas.width / 2);
    this.y = this.y + (canvas.height);

    if (mouse.x - canvas.width / 2 < 0) {
        this.dx = -this.dx;
    }

    this.dy = Math.sin(this.source.angle) * 8;
    this.dx = Math.cos(this.source.angle) * 8;
};