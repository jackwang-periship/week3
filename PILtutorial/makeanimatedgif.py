'''
Created on Jun 11, 2017

@author: student
'''
import imageio


filenames = ['output/NatLoop.gif-0.gif',
             'output/NatLoop.gif-1.gif',
             'output/NatLoop.gif-2.gif',
             'output/NatLoop.gif-3.gif',
             'output/NatLoop.gif-4.gif',
             'output/NatLoop.gif-5.gif',
             'output/NatLoop.gif-6.gif',
             'output/NatLoop.gif-7.gif'
            ]
images = []
for filename in filenames:
    im_of_one = imageio.imread(filename)
    images.append(im_of_one)
imageio.mimsave('output/movie.gif', images, fps=3.5)
