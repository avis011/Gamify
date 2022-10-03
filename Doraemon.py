# On Screen Pet
import tkinter as tk


class OnScreenPet:
    def __init__(self):
        # Create the window
        self.window = tk.Tk()
        self.window.title('OnScreen Pet')
        self.window.geometry('800x600')
        self.window.resizable(False, False)
        # Creating a Canvas
        self.canvas = tk.Canvas(master=self.window, bg='black')
        # Add the canvas into the window
        self.canvas.pack(expand=True, fill=tk.BOTH, padx=2, pady=2)
        # Drawing the pet
        # Face
        # Create_Oval function takes the coordinates of top left and bottom right
        self.window.after(1000, self.blink)
        self.eye_open = True
        self.canvas.create_oval((200, 120, 600, 480), fill='#1E96D5')
        self.canvas.create_oval((235, 215, 565, 470), fill='#FFFFFF', outline='#000000', width=2)
        self.default_left_eye_pupil_cords = (367, 217, 393, 243)
        self.default_right_eye_pupil_cords = (407, 217, 433, 243)
        self.left_eye = self.canvas.create_oval((305, 150, 400, 270), fill='#FFFFFF', outline='#000000', width=2)
        self.right_eye = self.canvas.create_oval((400, 150, 495, 270), fill='#FFFFFF', outline='#000000', width=2)
        self.left_eye_pupil = self.canvas.create_oval(self.default_left_eye_pupil_cords, fill='#000000')
        self.right_eye_pupil = self.canvas.create_oval(self.default_right_eye_pupil_cords, fill='#000000')
        # Nose
        self.canvas.create_oval((380, 250, 420, 290), fill='#FF0000', width=0)
        self.nose_shine = self.canvas.create_oval((385, 255, 400, 270), fill='#FFFFFF', width=0, state='hidden')
        # moustache
        self.canvas.create_line((310, 280, 370, 295), width=2)
        self.canvas.create_line((290, 310, 370, 310), width=2)
        self.canvas.create_line((310, 340, 370, 325), width=2)

        self.canvas.create_line((430, 295, 490, 280), width=2)
        self.canvas.create_line((430, 310, 510, 310), width=2)
        self.canvas.create_line((430, 325, 490, 340), width=2)

        self.canvas.create_line((400, 290, 400, 428), width=2)

        # mouth
        self.mouth_regular = self.canvas.create_line((290, 375, 400, 480, 520, 375), width=2, fill='#FF0000', smooth=1)
        self.mouth_smiling = self.canvas.create_arc((290, 300, 520, 340), start=0, extent=-180, fill='#FF0000', width=0,
                                                    state='hidden')
        # game_vlaues
        self.eye_open = False
        self.does_blink = True
        self.pupil_position = 'CENTER'

        # register(with the windows mainloop) for event observation
        self.window.bind('<Enter>', self.mouse_over)
        self.window.bind('<Leave>', self.mouse_out)
        self.window.bind('<Motion>', self.mouse_move)
        # schedule a class to blink method
        # It keeps the window (application) alive
        # It observes events (happenings) and invokes event procedures
        self.window.mainloop()

    def blink(self):
        if self.does_blink:
            if self.eye_open:
                # eyelid hidden
                self.canvas.itemconfig(self.left_eye, fill='#FFFFFF')
                self.canvas.itemconfig(self.right_eye, fill='#FFFFFF')
                # eye pupil visible
                self.canvas.itemconfig(self.left_eye_pupil, state='normal')
                self.canvas.itemconfig(self.right_eye_pupil, state='normal')

            else:
                # eye lid visible
                self.canvas.itemconfig(self.left_eye, fill='#1E96D5')
                self.canvas.itemconfig(self.right_eye, fill='#1E96D5')
                # eye pupil hidden
                self.canvas.itemconfig(self.left_eye_pupil, state='hidden')
                self.canvas.itemconfig(self.right_eye_pupil, state='hidden')

            # for the next call
            self.eye_open = not self.eye_open
        else:
            if self.eye_open:
                # eyelid hidden
                self.canvas.itemconfig(self.left_eye, fill='#FFFFFF')
                self.canvas.itemconfig(self.right_eye, fill='#FFFFFF')
                # eye pupil visible
                self.canvas.itemconfig(self.left_eye_pupil, state='normal')
                self.canvas.itemconfig(self.right_eye_pupil, state='normal')
                self.eye_open = True

        # schedule a call to blink method
        self.window.after(3000, self.blink)

    def mouse_over(self, event):
        self.does_blink = False
        self.canvas.itemconfig(self.nose_shine, state='normal')
        self.canvas.itemconfig(self.mouth_regular, state='hidden')
        self.canvas.itemconfig(self.mouth_smiling, state='normal')

    def mouse_out(self, event):
        self.does_blink = True
        self.canvas.itemconfig(self.nose_shine, state='hidden')
        self.canvas.itemconfig(self.mouth_regular, state='normal')
        self.canvas.itemconfig(self.mouth_smiling, state='hidden')
        self.canvas.coords(self.left_eye_pupil, self.default_left_eye_pupil_cords)
        self.canvas.coords(self.right_eye_pupil, self.default_right_eye_pupil_cords)

    def mouse_move(self, event):

        if event.y < self.default_left_eye_pupil_cords[1] and event.x >= self.default_left_eye_pupil_cords[
            0] and event.x <= self.default_right_eye_pupil_cords[2]:
            self.pupil_position = 'TOP'
        if event.y >= self.default_left_eye_pupil_cords[1] and event.y <= self.default_left_eye_pupil_cords[
            3] and event.x >= self.default_left_eye_pupil_cords[0] and event.x <= self.default_right_eye_pupil_cords[2]:
            self.pupil_position = 'CENTER'
        if event.y > self.default_left_eye_pupil_cords[3] and event.x >= self.default_left_eye_pupil_cords[
            0] and event.x <= self.default_right_eye_pupil_cords[2]:
            self.pupil_position = 'BOTTOM'

        if event.y < self.default_left_eye_pupil_cords[1] and event.x < self.default_left_eye_pupil_cords[0]:
            self.pupil_position = 'TOPLEFT'
        if event.y >= self.default_left_eye_pupil_cords[1] and event.x < self.default_left_eye_pupil_cords[0]:
            self.pupil_position = 'LEFT'
        if event.y > self.default_left_eye_pupil_cords[3] and event.x < self.default_left_eye_pupil_cords[0]:
            self.pupil_position = 'BOTTOMLEFT'

        if event.y < self.default_left_eye_pupil_cords[1] and event.x > self.default_right_eye_pupil_cords[2]:
            self.pupil_position = 'TOPRIGHT'
        if event.y >= self.default_left_eye_pupil_cords[1] and event.x > self.default_right_eye_pupil_cords[2]:
            self.pupil_position = 'RIGHT'
        if event.y > self.default_left_eye_pupil_cords[3] and event.x > self.default_right_eye_pupil_cords[2]:
            self.pupil_position = 'BOTTOMRIGHT'

        lx1, ly1, lx2, ly2 = self.default_left_eye_pupil_cords
        rx1, ry1, rx2, ry2 = self.default_right_eye_pupil_cords

        if self.pupil_position == 'CENTER':
            lx1, ly1, lx2, ly2 = self.default_left_eye_pupil_cords
            rx1, ry1, rx2, ry2 = self.default_right_eye_pupil_cords

        elif self.pupil_position == 'TOP':
            ly1 -= 40
            ly2 -= 40
            ry1 -= 40
            ry2 -= 40

        elif self.pupil_position == 'BOTTOM':
            ly1 += 10
            ly2 += 10
            ry1 += 10
            ry2 += 10

        elif self.pupil_position == 'TOPLEFT':
            ly1 -= 40
            ly2 -= 40
            ry1 -= 40
            ry2 -= 40
            lx1 -= 20
            lx2 -= 20
            rx1 -= 2
            rx2 -= 2

        elif self.pupil_position == 'LEFT':
            lx1 -= 20
            lx2 -= 20
            rx1 -= 2
            rx2 -= 2

        elif self.pupil_position == 'BOTTOMLEFT':
            ly1 += 10
            ly2 += 10
            ry1 += 10
            ry2 += 10
            lx1 -= 20
            lx2 -= 20
            rx1 -= 2
            rx2 -= 2

        elif self.pupil_position == 'TOPRIGHT':
            ly1 -= 40
            ly2 -= 40
            ry1 -= 40
            ry2 -= 40
            lx1 += 2
            lx2 += 2
            rx1 += 20
            rx2 += 20
        elif self.pupil_position == 'RIGHT':
            lx1 += 2
            lx2 += 2
            rx1 += 20
            rx2 += 20
        elif self.pupil_position == 'BOTTOMRIGHT':
            ly1 += 10
            ly2 += 10
            ry1 += 10
            ry2 += 10
            lx1 += 2
            lx2 += 2
            rx1 += 20
            rx2 += 20

        self.canvas.coords(self.left_eye_pupil, (lx1, ly1, lx2, ly2))
        self.canvas.coords(self.right_eye_pupil, (rx1, ry1, rx2, ry2))


def main():
    pet = OnScreenPet()


main()
