import os
#Save Training and test images in their respective folders
def saveFiles(Genotypes):
     for i in range(len(Genotypes)):
            for idx in range(len(Genotypes[i].trainSet)):
                save_fname0 = os.path.join(Genotypes[i].train_path, 'Train' + str(idx+1) + '.png')
                Genotypes[i].trainSet[idx].save(save_fname0)
            for idx in range(len(Genotypes[i].testSet)):
                save_fname0 = os.path.join(Genotypes[i].test_path, 'Test' + str(idx+1) + '.png')
                Genotypes[i].testSet[idx].save(save_fname0)