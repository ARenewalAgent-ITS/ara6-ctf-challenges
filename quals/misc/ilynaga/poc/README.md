# Writeup 📝

For this challenge, it's really just an adversarial perturbation attack on the image classifier, you can use whatever technique you want, as long as the SSIM stays within the minimum of 0.96.

The intended solver is in [solver.py](./solver.py), it's a pretty simple BIM implemented in tensorflow under $L_2$ norm. The reason why I used BIM is mostly just for simplicity's sake, I couldn't for the life of me get TF wrapped ard my head lol, sadge.

## Further thoughts

Fwiw, the only thing that *might* trip you up is the localization of the perturbation that needs to be done, since deepface isolates the face out internally when `.verify()` is called, so if you don't follow that, you're just wasting effort, but beyond that, the perturbation should converge fine. This helps a lot too, since SSIM gets really bad afaict on tiny patches lol.

Anyway, I'd wanted to use a more robust model, Deepface's default VGG seems to perform *significantly* worse from my personal testing when it came down to adversarially-perturbed inputs. I considered Facenet512, which was much larger, slower, and much more robust in my testing, but since I'd considered that it might've been too much given the timeframe, I decided to put it off, since some players might not even be familiar with ML attacks.

*Technically*, you can run PGD just fine here, but I just cba making a PGD in TF. They're practically equivalent definition-wise mathematically[^1], basically just, 

```math
x^{t+1} = \textit{Clip}_{x, \epsilon}\{x^t + \alpha sign(\nabla_\textit{x}\ L(\theta, x, y))\}
```

barring implementation details anyway (assuming $L_{\infty}$ norm), so 🤷

Might be able to get better results with $L_0$ mechanisms too, feel free to try those out :)

[^1]: Madry, Aleksander, et al. Towards Deep Learning Models Resistant to Adversarial Attacks. 2019, https://arxiv.org/abs/1706.06083.