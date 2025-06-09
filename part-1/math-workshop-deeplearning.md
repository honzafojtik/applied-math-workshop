# Deep Learning Workshop  
_Maths in (deep) neural networks for image classification_

---

## 1 Why it matters  
- Photo apps tag people; self‑driving cars spot obstacles; medical scanners flag anomalies.  
- All start by converting pixels into numbers, then “learning” patterns in the sequences.  


---

## 2 Picture to numbers  
> Every image is a tensor of pixel values

| image type   | tensor notation                         | shape               |
|--------------|-----------------------------------------|---------------------|
| **grayscale**| X ∈ ℝ^{H×W}      | H × W     | 
| **RGB color**| X ∈ ℝ^{3×H×W} | 3 × H × W |

Values are usually scaled to [0,1].


<img src="https://github.com/user-attachments/assets/9849786e-ba00-43ad-bdc4-80d70a06d0d6" width="700"/>

---

## 3 Weights & Biases  
> How the network learns

- **Weights** (W): determine how much each input contributes.  
  For inputs x₁, x₂ with weights w₁, w₂:
  
      weighted sum = w₁ × x₁ + w₂ × x₂
A larger wᵢ makes xᵢ more influential; a negative wᵢ makes it ignore certain features.

- **Biases** (b): a constant added after the weighted sum, shifting the result.  
  Together:
  
      z = w₁ × x₁ + w₂ × x₂ + b
  Even if all inputs are zero, b lets the neuron output a non‑zero value.


---
## 4 Activation Functions  
> Adding flexibility with non‑linearity

After computing z, we apply f(z) so the neuron can model curves instead of straight lines. Without this step, a neural network made of only linear operations would itself be linear. That means it couldn’t learn complex shapes, patterns, or decision boundaries like 

  "if pixel brightness is above a threshold, call it a cat."

The activation function introduces **non-linearity**, which lets the network learn more complex patterns.

| Name    | Formula            | Output range | What it does                                                                              |
|---------|---------------------------|--------------|--------------------------------------------------------------------------------------------|
| ReLU    | max(0, z)          | 0 to ∞       | Sets all negative values to 0; positive values stay the same                              |
| Sigmoid | 1 / (1 + e^(−z))   | 0 to 1       | Converts any input into a value between 0 and 1; extreme values become very close to 0 or 1 |
| Tanh    | tanh(z)            | –1 to 1      | Like sigmoid, but outputs are centered around 0; negative inputs produce negative outputs  |
| Linear  | f(z) = z           | –∞ to ∞      | Doesn’t change the input at all, just passes it through (used only for comparison)                                |

<img src="./assets/activation-functions.jpg" width="600"/>

---

## 5 Building a Network  
> Stacking neurons into layers

Neural networks are built by combining many simple units called **neurons**. Each neuron takes in numbers, applies a weighted sum and an activation function, and sends the result forward.

This diagram shows a typical network made of:
- **Input layer**: the raw input features (like pixel values in an image)
- **Hidden layers**: several layers of neurons that transform the input step by step
- **Output layer**: final predictions, like class scores

Each neuron in a layer connects to **every neuron in the next layer**. These are called **fully connected** (or dense) layers.

<img src="./assets/layers.png" width="600"/>

### 5.1 Linear (hidden) layers

Each hidden layer in a neural network usually performs two steps:
1. A **linear transformation**:   Wx + b  
2. A **non-linear activation**:   f(Wx + b)

So the full output of a layer is:

    y = f(Wx + b)

Where:
- x ∈ ℝ^{d_in}  input vector
- W ∈ ℝ^{d_out×d_in}  weight matrix
- b ∈ ℝ^{d_out}  bias vector
- f = activation function (see Section 4)

A **layer** is many of these neurons in parallel.  
A **network** is just many layers stacked together.

- Early layers learn basic features like edges  
- Middle layers combine them into shapes or parts  
- Later layers learn complete objects or categories

---

## 6 Architectures: CNN vs ViT  
There are various architecture types used in image classification tasks, however the Convolutional Neural Network (CNN) and Vision Transformer (ViT) are most commonly used:
- **CNN**: local receptive field via filters going over an image.  
- **ViT**: global receptive field via attention mechanism.

<img src="./assets/CNN-vs-ViT.png" width="600"/>

### 6.1 Convolutional Neural Network (CNN)  
> focusing on local patterns

A Convolutional Neural Network: 
- Captures edges, corners, textures within local neighborhoods.  
- Is efficient with a few parameters and fast computations.
  
A small kernel \(K\) slides over the image \(X\), reusing the same weights:

    Y[cₒ, h, w] = ∑₍cᵢ₎ ∑ₘ ∑ₙ K[cₒ, cᵢ, m, n] × X[cᵢ, h + m, w + n]

Where 

    Y[cₒ, h, w]
    
is the output value at location (h, w) in output channel cₒ, and

    ∑₍cᵢ₎ ∑ₘ ∑ₙ

which means we sum over input channels and over each kernel position where

    K[cₒ, cᵢ, m, n]
    
is the kernel weight connecting input channel cᵢ to output channel cₒ at offset (m, n) and where

    X[cᵢ, h + m, w + n]
    
is the input pixel at location (h + m, w + n) in input channel cᵢ


### 6.2 Vision Transformer (ViT)  
> looking at the whole image globally

A Vision Transformer:

- Looks at all patches at once using self-attention
- Captures long-range structure and image-wide context

The image is first split into fixed-size patches, flattened, and embedded:

    zᵢ = xᵢ × E + pᵢ

where

  zᵢ
is the final input embedding for patch i

  xᵢ
is the flattened pixel vector of patch i

  E
is a learned linear projection (shared across patches)

  pᵢ
is the positional encoding for patch i, indicating its location in the image

These embedded patches are then passed into the transformer. Inside it, self-attention is applied:

    Attention(Q, K, V) = softmax(QKᵀ / √d) × V
    
Where

  Q, K, V
are query, key, and value vectors derived from the embedded patches

  d
is the dimensionality of the key vectors (used to scale the dot product)

At the start of the sequence, a special token (CLS) is added. After processing, its output contains a summary of the whole image and is used for classification.


---

## 7 Making a Prediction – Softmax  
> turn raw scores into probabilities

Given final scores (logits) \(z_i\) for each class \(i\):

\[
p_i = \frac{e^{z_i}}{\displaystyle\sum_{j=1}^C e^{z_j}}
\]

- All \(p_i\) lie in \([0,1]\) and sum to 1.  
- The highest \(p_i\) is the predicted class.

---

## 8 Teaching the Network – Loss Functions  

### 8.1 Cross‑Entropy Loss  
Used when classes are fairly balanced.

\[
\mathcal{L}_{CE}(y,\hat y)
= -\sum_{i=1}^C y_i \,\log(\hat y_i)
\]

- \(y_i\): true label (one‑hot vector)  
- \(\hat y_i\): predicted probability  

A big penalty if the network assigns low \(\hat y\) to the true class.

### 8.2 Focal Loss  
Helps when some classes are rare.

\[
\mathcal{L}_{focal}(y,\hat y)
= -\sum_{i=1}^C \alpha_i\,(1 - \hat y_i)^\gamma\,y_i\,\log(\hat y_i)
\]

- \(\alpha_i\): weight for class \(i\) to balance frequencies.  
- \(\gamma>0\): focusing factor that down‑weights well‑classified examples.



---

## 9 Learning Loop  
> training in 5 steps

1. **Forward pass**: image → network → logits → softmax → probabilities  
2. **Compute loss**: cross‑entropy or focal  
3. **Back‑propagation**: compute gradients \(\nabla_\theta \mathcal{L}\) for all \(W, b\)  
4. **Update**:  
   \[
   \theta \leftarrow \theta - \eta\,\nabla_\theta \mathcal{L}
   \]  
5. Repeat over many images until performance stops improving.

---

## 10 Key Takeaways

- **Pixels → tensors** feed into math pipelines.  
- **Weights & biases** are the only learned parameters.  
- **Affine + activation** lets neurons learn curves, not just lines.  
- **CNNs** capture local patterns; **ViTs** capture global context.  
- **Softmax + loss** provide a clear training signal.  
- **Back‑prop + gradient descent** tune the weights and biases.  
- **Focal loss** helps when some classes are much rarer than others.
