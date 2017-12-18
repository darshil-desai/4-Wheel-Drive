
# coding: utf-8

# In[5]:


import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig1 = plt.figure()
ax1 = fig1.add_subplot(111, aspect='equal')
ax1.add_patch(
    patches.Rectangle(
        (0.1, 0.1),   # (x,y)
        1,          # width
        10,          # height
    )
)
fig1.savefig('rect1.png', dpi=90, bbox_inches='tight')
plt.show()

