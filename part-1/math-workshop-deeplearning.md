# Deep Learning Workshop  
_A precise, code‑free walkthrough of the core mathematics behind image classification with neural networks._


---

## 1 Input → Tensor  
> how do we feed an image to math?

| image type   | tensor notation                         | shape               |
|--------------|-----------------------------------------|---------------------|
| **grayscale**| \(X \in \mathbb{R}^{H \times W}\)       | \(H \times W\)      |
| **RGB color**| \(X \in \mathbb{R}^{3 \times H \times W}\) | \(3 \times H \times W\) |

![](./assets/3-axis_front.png)

Pixels are real numbers, typically scaled to \([0,1]\).

---

## 2 Weights & Biases  
> the parameters the network learns

- **Weights** (\(W\)): determine how much each input contributes.  
  For inputs \(x_1, x_2\) with weights \(w_1, w_2\):  
  \[
    \text{weighted sum} = w_1 \times x_1 + w_2 \times x_2
  \]  
  A larger \(w_i\) makes \(x_i\) more influential; a negative \(w_i\) flips its effect.

- **Biases** (\(b\)): a constant added after the weighted sum, shifting the result.  
  Together:  
  \[
    z = w_1 x_1 + w_2 x_2 + b
  \]  
  Even if all inputs are zero, \(b\) lets the neuron output a non‑zero value.

This multiply‑then‑add step is called an **affine transformation**.

---

## 3 Layers in a network 
> building blocks of the network

![](./assets/layers.png)

### 3.1 Linear (hidden) layers  
\[
\boxed{y = f(Wx + b)}
\]  
- \(x\in\mathbb{R}^{d_{\text{in}}}\): input vector (flattened)  
- \(W\in\mathbb{R}^{d_{\text{out}}\times d_{\text{in}}}\): weights  
- \(b\in\mathbb{R}^{d_{\text{out}}}\): bias  
- \(f\): activation (see §4)

---

## 4 Activation Functions  
> adding non‑linearity

| name        | formula                                   | note                                         |
|-------------|-------------------------------------------|----------------------------------------------|
| **Linear**  | \(f(x) = x\)                              | identity; often used in output layer         |
| **ReLU**    | \(\max(0, x)\)                            | default; avoids vanishing gradient for \(x>0\) |
| **Sigmoid** | \(\tfrac{1}{1 + e^{-x}}\)                 | squashes to \((0,1)\)                        |
| **Tanh**    | \(\tfrac{e^{x} - e^{-x}}{e^{x} + e^{-x}}\) | zero‑centred                                 |

![](./assets/activation-functions.jpg)

---

## 5 Architectures: CNNs vs. ViTs  

### 5.1 Convolutional Neural Networks (CNN)  
> learning local patterns

\[
Y_{c_o,h,w}
=
\sum_{c_i=1}^{C_{\text{in}}}
\sum_{m=0}^{k-1}
\sum_{n=0}^{k-1}
K_{c_o,c_i,m,n}\;
X_{c_i,\,h+m,\,w+n}
\]

- \(K\): shared‑weight kernel  
- stride/padding control output size  

![](./assets/cnn-feature-hierarchy.png)

### 5.2 Vision Transformers (ViTs)  
> a global‑attention alternative

1. **Patchify**: split image into \(N\) patches, flatten to vectors \(x_i\)  
2. **Embed**: linear projection + position embedding  
3. **Self‑attention**:  
   \[
   \mathrm{Attn}(Q,K,V)
   =
   \operatorname{softmax}\!\Bigl(\tfrac{QK^\top}{\sqrt d}\Bigr)\,V
   \]  
4. **CLS token** gathers patch information into a single vector  

![](./assets/vit-attention.png)

### 5.3 CNN vs. ViT  

- **CNN**: Uses kernels (filters) to detect local features 
- **ViT**: Uses attention mechanism to learn relationships between all features

![](./assets/CNN-vs-ViT.png)

---

## 6 Softmax → Class Probabilities  
> turning raw scores into a distribution

Given logits \(z\in\mathbb{R}^C\):

\[
\operatorname{softmax}(z)_i
=
\frac{e^{z_i}}{\sum_{j=1}^C e^{z_j}}
\]

Produces \(p\in[0,1]^C\) with \(\sum_i p_i=1\).

---

## 7 Loss: Cross‑Entropy vs. Focal  
> teaching the network from its mistakes

### 7.1 Cross‑Entropy  
\[
\mathcal L_{\text{CE}}(y,\hat y)
=
-\sum_{i=1}^C y_i \,\log(\hat y_i)
\]  
- \(y\): one‑hot true label  
- \(\hat y\): predicted probability  

### 7.2 Focal Loss  
\[
\mathcal L_{\text{focal}}(y,\hat y)
=
-\sum_{i=1}^C \alpha_i\,(1 - \hat y_i)^\gamma\,y_i\,\log(\hat y_i)
\]  
- \(\alpha_i\): class weight  
- \(\gamma>0\): focusing parameter  
- down‑weights easy (well‑classified) examples  

![](./assets/ce-vs-focal.png)

---

## 8 Learning Loop  
> training in 5 steps

1. **Forward pass** → logits → softmax → probabilities  
2. **Compute loss** (cross‑entropy or focal)  
3. **Back‑propagation** → gradients \(\nabla_\theta \mathcal L\)  
4. **Update** weights & biases:  
   \[
   \theta \leftarrow \theta - \eta\,\nabla_\theta \mathcal L
   \]
5. Repeat until the network converges

---

## 9 Minimal Forward Pass (Symbolic)

1. **Normalize**: \(\tilde X = X/255\)  
2. **Conv + ReLU**: \(H_1 = \mathrm{ReLU}(W_1 * \tilde X + b_1)\)  
3. **Conv + ReLU**: \(H_2 = \mathrm{ReLU}(W_2 * H_1 + b_2)\)  
4. **Flatten**: \(h = \mathrm{vec}(H_2)\)  
5. **Dense**: \(z = W_3\,h + b_3\)  
6. **Softmax**: \(\hat y = \mathrm{softmax}(z)\)

---

## 10 Key Takeaways

- **Images → tensors** become inputs to math pipelines  
- **Weights & biases** (\(W, b\)) are the only parameters learned  
- **CNNs** exploit local structure; **ViTs** exploit global attention  
- **Softmax + loss** convert logits into a learning signal  
- **Back‑propagation + gradient descent** adjust every weight  
- **Focal loss** helps when classes are imbalanced  

All “intelligence” resides in the optimized values of \(W\) and \(b\).  
