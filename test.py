import torch

from sklearn.metrics import roc_auc_score


def eval(self, net, c, dataloader):
    """Testing the Deep SVDD model"""

    scores = []
    labels = []
    net.eval()
    print('Testing...')
    with torch.no_grad():
        for x, y in dataloader:
            x = x.float().to(self.device)
            z = net(x)
            score = torch.mean(torch.sum((z - c) ** 2, dim=1))

            scores.append(score.detach().cpu())
            labels.append(y.cpu())
    labels, scores = torch.cat(labels).numpy(), torch.cat(scores).numpy()
    print('ROC AUC score: {:.3f}'.format(roc_auc_score(labels, scores)))
    return labels, scores