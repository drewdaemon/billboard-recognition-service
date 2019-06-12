from imageio import imread
from manager.manager import ImageManager
from sklearn.metrics import accuracy_score

train_paths = ['train/1.png', 'train/2.png', 'train/3.png', 'train/4.png']
test_paths = ['test/1.png', 'test/2.png', 'test/3.png', 'test/4.png']

train_imgs = [imread(path) for path in train_paths]
test_imgs = [imread(path) for path in test_paths]

manager = ImageManager()

train_ids = []
for img in train_imgs:
    train_ids.append(manager.register(img))

predictions = []
for img in train_imgs:
    predictions.append(manager.predict(img))

accuracy = accuracy_score(train_ids, predictions)
print(f'Accuracy: {accuracy}')

