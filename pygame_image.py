import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        bg_move = tmr % 3200
        screen.blit(bg_img, [-bg_move, 0])
        screen.blit(bg_img2, [-bg_move + 1600, 0])
        screen.blit(bg_img, [-bg_move + 3200, 0])
        #screen.blit(bg_img2, [-bg_move + 4800, 0])
        #bg_img_rct = bg_img.get_rect()
        #bg_img_rct.right = 0, 0 #rectの中心位置
        kk_img_rct = kk_img.get_rect() #こうかとんのrect抽出
        kk_img_rct.center = 300, 200 #rectの中心位置
        screen.blit(kk_img, kk_img_rct)
        pg.display.update()
        tmr += 1     
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()