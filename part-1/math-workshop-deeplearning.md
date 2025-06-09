# Deep Learning Workshop  
_Maths in (deep) neural networks for image classification_

---

## 1 Why it matters  
- Photo apps tag people; self‑driving cars spot obstacles; medical scanners flag anomalies.  
- All start by converting pixels into numbers, then “learning” patterns in the sequences.  

---

## 2 Picture to numbers  
> Every image is a tensor of pixel values

Neural networks cannot work directly with image files like .jpg or .png.  
Instead, each image is converted into a grid of numbers: one number per pixel.  
These numbers represent brightness (in grayscale) or color intensity (in RGB).  
The result is a **tensor** — a multi-dimensional array that stores all pixel values.

| image type   | tensor notation           | shape       |
|--------------|---------------------------|-------------|
| **grayscale**| X ∈ ℝ<sup>H×W</sup>       | H × W       |
| **RGB color**| X ∈ ℝ<sup>3×H×W</sup>     | 3 × H × W   |

Each pixel value is typically scaled to fall between **0 and 1** before being passed to the model.

**Example:**  
The left image below shows a grayscale image stored as a 2D array with height `H` and width `W`.  
The right image shows a color image where each color channel (Red, Green, Blue) is stored separately.  
These 3 channels are stacked to form a 3D tensor with shape `C × H × W`, where `C = 3`.

![Tensor shape diagram](/mnt/data/1548ea1b-35c5-4100-b65e-71245d1cb706.png)

---

## 3 Weights & Biases  
> How the network learns

Each connection in a neural network has a **weight** (`w`) and each neuron has a **bias** (`b`).  
These are the main values the model adjusts during training.

- **Weights** (W): determine how much each input contributes.  
  For inputs x₁, x₂ with weights w₁, w₂:

      weighted sum = w₁ × x₁ + w₂ × x₂

  A larger wᵢ makes xᵢ more important; a negative wᵢ means xᵢ has a reducing or canceling effect.  
  The network changes the weights during training to learn what matters in the input.

- **Biases** (b): a fixed number added after the weighted sum.  
  It shifts the output up or down:

      z = w₁ × x₁ + w₂ × x₂ + b

  Without a bias, the output would always be zero when all inputs are zero.  
  The bias allows the neuron to produce a non-zero output even in that case.  
  This gives the model more flexibility and helps it fit patterns in the data better.

Weights and biases are the **parameters** the network learns. These values decide what the model does and how it responds to different inputs.

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

## 5.1 Linear (hidden) layers
A **linear layer** is one of the basic components in a neural network. It takes an input, multiplies it by a weight matrix, adds a bias, and applies an activation function. Each hidden layer in a neural network usually performs two steps:  

1. A **linear transformation**:   `Wx + b`  
2. A **non-linear activation**:   `f(Wx + b)`

So the full output of a layer is:

    y = f(Wx + b)

Where:  
- `x` is the input vector  
- `W` is the weight matrix  
- `b` is the bias vector  
- `f` is the activation function (see Section 4)

A hidden **layer** performs this transformation for many neurons in parallel.  
A **network** consists of many of these layers stacked in sequence.

Early layers learn basic features like edges and color gradients.  
Middle layers combine these into more complex patterns or shapes.  
Later layers detect high level structures like objects or categories.


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

- `zᵢ`
is the final input embedding for patch i

- `xᵢ`
is the flattened pixel vector of patch i

- `E`
is a learned linear projection (shared across patches)

- `pᵢ`
is the positional encoding for patch i, indicating its location in the image

These embedded patches are then passed into the transformer. Inside it, self-attention is applied:

    Attention(Q, K, V) = softmax(QKᵀ / √d) × V
    
Where

  `Q`, `K`, `V`
are query, key, and value vectors derived from the embedded patches

  `d`
is the dimensionality of the key vectors (used to scale the dot product)

At the start of the sequence, a special token (CLS) is added. After processing, its output contains a summary of the whole image and is used for classification.


---

## 7 Making a Prediction – Softmax  
> turn raw scores into probabilities

At the end of a classification network, we get one score for each class.  
These are called **logits** and are not yet probabilities.

The **softmax** function turns these logits into a probability distribution:

    p_i = exp(z_i) / sum_j exp(z_j)

Where:  
- `z_i` is the score for class `i`  
- `p_i` is the predicted probability for class `i`  
- The sum runs over all classes `j = 1 to C`

This ensures:  
- All `p_i` values lie between 0 and 1  
- The total sum of `p_i` over all classes is 1  
- The class with the highest `p_i` is the predicted label

**Example:**  
A model predicts the classes **cat**, **dog**, and **car**, and outputs the following logits:

    cat: 2.0  
    dog: 1.0  
    car: 0.1

Apply the softmax function:

    exp(2.0) ≈ 7.39  
    exp(1.0) ≈ 2.72  
    exp(0.1) ≈ 1.11  
    sum ≈ 11.22

Compute probabilities:

    cat: 7.39 / 11.22 ≈ 0.66  
    dog: 2.72 / 11.22 ≈ 0.24  
    car: 1.11 / 11.22 ≈ 0.10

The predicted class is **cat**, with the highest probability.


---

## 8 Teaching the Network – Loss Functions  

### 8.1 Cross‑Entropy Loss  
Used when classes are fairly balanced.

Cross-entropy loss:

    L_CE(y, ŷ) = -∑ y_i * log(ŷ_i)

- `y_i` true label (one-hot vector)  
- `ŷ_i` predicted probability for class i  

A big penalty if the network assigns low probability to the true class.  
The loss is **0** when the model assigns 100% probability to the correct class.  
The loss increases when the confidence in the wrong class increases.

**Example:**  
True class: **dog**  
Predicted probabilities:

    cat: 0.01  
    dog: 0.95  
    car: 0.04

Cross-entropy loss:  
Only the correct class (dog) contributes, so:

    Loss = -log(0.95) ≈ 0.05

Now imagine a bad prediction:

    cat: 0.80  
    dog: 0.10  
    car: 0.10

    Loss = -log(0.10) ≈ 2.30

Higher loss = worse prediction.


### 8.2 Focal Loss  
Helps when some classes are rare or imbalanced in volume.

Focal loss:

    L_focal(y, ŷ) = -∑ α_i * (1 - ŷ_i)^γ * y_i * log(ŷ_i)

- `α_i` weight for class i to balance class volumes  
- `γ > 0` focusing factor that down weights easy to classify examples  

Focal loss adds two things to cross entropy:  
It gives more weight to rare classes (via `α`), and reduces the loss for well-classified examples (via `γ`).  
This makes the model focus on harder or rarer cases.

**Example:**  
True class: **dog**  
Parameters:  
α_dog = 1.0, γ = 2.0  
Predicted probabilities:

    cat: 0.01  
    dog: 0.95  
    car: 0.04

Focal loss:  
Only the correct class (dog) contributes, so:

    Loss = -1.0 * (1 - 0.95)^2 * log(0.95)  
         = -1.0 * 0.0025 * (-0.051)  
         ≈ 0.00013

Now imagine a bad prediction:

    cat: 0.80  
    dog: 0.10  
    car: 0.10

    Loss = -1.0 * (1 - 0.10)^2 * log(0.10)  
         = -1.0 * 0.81 * (-2.302)  
         ≈ 1.86

Focal loss is low when the prediction is confident and correct, and high when the model is wrong and uncertain.

---

## 9 Learning Loop  
> Training in 5 steps

In a script that contains the entire training process, five steps are repeated:

1. **Forward pass**:  
   The input image is passed through the network. Each layer transforms the data until the final output (logits) are produced. Softmax then converts these logits into probabilities.

2. **Compute loss**:  
   The predicted probabilities are compared to the true label. A loss function (e.g. cross-entropy or focal loss) calculates how wrong the prediction is. Lower loss means better prediction.

3. **Backpropagation**:  
   The model calculates how much the loss (L) would change if each parameter (θ) were adjusted.  
   This is done by computing the gradient: `∇θ L`.  
   The symbol `∇` (nabla) means “rate of change” — it tells us how sensitive the loss is to each parameter.  
   The gradient points in the direction that increases the loss the most.  
   The model uses this information to update the parameters in the opposite direction.  
   (`θ` includes all learnable weights and biases in the network.)

4. **Update**:  
   The optimizer adjusts the parameters using the gradients:  

       θ ← θ - η * ∇θ L  

   where `η` is the learning rate: a small number that controls how big each step is. This step moves the model in the direction that reduces the loss.

5. **Repeat**:  
   These steps are repeated for many epochs where `1 epoch = 1 x total dataset`.  
   Training stops when the performance no longer improves on the validation set.


---

## 10 Key Takeaways

- **Pixels → tensors** used for learning features.  
- **Weights & biases** are the only learned parameters.  
- **Affine + activation** lets neurons learn curves, not just lines.  
- **CNNs** capture local patterns; **ViTs** capture global context.  
- **Softmax + loss** provide a clear training signal.  
- **Back‑prop + gradient descent** tune the weights and biases.  
- **Focal loss** helps when some classes are much rarer than others.
