import numpy as np
import shortuuid
from sklearn.neighbors import KNeighborsClassifier
from .feature_extractor import FeatureExtractor

class ImageManager:

    def __init__(self):
        self.photo_ids = []
        self.extractor = FeatureExtractor()
        self.features = None
        self.classifier = KNeighborsClassifier(n_neighbors=1)

    def register(self, img):
        img_feature = self.extractor.extract_features(img)
        if self.features is not None:
            self.features = np.vstack((self.features, img_feature))
        else:
            self.features = np.expand_dims(img_feature, axis=0)

        photo_id = shortuuid.uuid()
        self.photo_ids.append(photo_id)
        return photo_id

    def register_mult(self, imgs):
        raise NotImplementedError()

    def predict(self, img):
        test_feature = self.extractor.extract_features(img)
        # X is self.features normalized by column
        X = self.features / (self.features.max(axis=0) + .0000000000001)
        y = np.arange(len(self.photo_ids))
        self.classifier.fit(X, y)
        prediction = self.classifier.predict(test_feature.reshape(1,-1))

        return self.photo_ids[prediction[0]]
